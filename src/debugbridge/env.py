"""Detect whether Windows Debugging Tools are installed.

pybag raises ``FileNotFoundError`` at import time when ``dbgeng.dll`` is
missing, so we check for Debugging Tools *before* ever importing pybag. This
module has no pybag dependency and is safe to import on any platform.
"""

from __future__ import annotations

import os
import shutil
from dataclasses import dataclass, field
from pathlib import Path

# Canonical install location for the x64 Debugging Tools.
# pybag hard-codes this same path when loading dbgeng.dll.
CANONICAL_DEBUGGERS_X64 = Path(r"C:\Program Files (x86)\Windows Kits\10\Debuggers\x64")

# Executables and DLLs we need. dbgsrv.exe is used to host remote attach;
# cdb.exe is the command-line debugger; the DLLs are what pybag actually loads.
REQUIRED_EXES = ("dbgsrv.exe", "cdb.exe")
REQUIRED_DLLS = ("dbgeng.dll", "symsrv.dll", "dbghelp.dll")

INSTALL_GUIDANCE = (
    "Windows Debugging Tools are required. Install via one of:\n"
    "  1. Windows SDK installer → select the 'Debugging Tools for Windows' component\n"
    "     https://learn.microsoft.com/windows-hardware/drivers/debugger/\n"
    "  2. Run scripts/install-debugging-tools.ps1 (bundled with DebugBridge)\n"
    f"Expected install path: {CANONICAL_DEBUGGERS_X64}\n"
    "After install, make sure that path is on your PATH, then re-run 'debugbridge doctor'."
)


@dataclass
class EnvCheckResult:
    """Outcome of an environment check."""

    ok: bool
    found: dict[str, str] = field(default_factory=dict)  # name → resolved path
    missing: list[str] = field(default_factory=list)
    guidance: str | None = None


def _find_on_path_or_canonical(name: str) -> str | None:
    """Look for an executable/DLL on PATH, falling back to the canonical SDK location."""
    on_path = shutil.which(name)
    if on_path:
        return on_path
    candidate = CANONICAL_DEBUGGERS_X64 / name
    if candidate.exists():
        return str(candidate)
    return None


def check_debugging_tools() -> EnvCheckResult:
    """Return a structured report of what's installed and what's missing."""
    found: dict[str, str] = {}
    missing: list[str] = []

    for name in (*REQUIRED_EXES, *REQUIRED_DLLS):
        resolved = _find_on_path_or_canonical(name)
        if resolved:
            found[name] = resolved
        else:
            missing.append(name)

    ok = not missing
    return EnvCheckResult(
        ok=ok,
        found=found,
        missing=missing,
        guidance=None if ok else INSTALL_GUIDANCE,
    )


def ensure_dbgeng_on_path() -> None:
    """Prepend the canonical debuggers directory to PATH for the current process.

    pybag uses ``ctypes.windll.LoadLibrary`` which respects the current PATH.
    When the user has Debugging Tools installed in the canonical location but
    hasn't added it to PATH, we still want to work.
    """
    if not CANONICAL_DEBUGGERS_X64.exists():
        return
    current = os.environ.get("PATH", "")
    canonical = str(CANONICAL_DEBUGGERS_X64)
    if canonical not in current:
        os.environ["PATH"] = f"{canonical}{os.pathsep}{current}"
