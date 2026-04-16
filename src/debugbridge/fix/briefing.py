"""Crash-briefing assembly (task 2a.1.3 - source-snippet extractor half).

``extract_source_snippets`` walks a call stack, resolves in-repo file paths,
merges overlapping plus/minus N-line ranges per file, and returns a dict of
``repo-relative Path -> snippet string`` for use by the briefing renderer
(landing in task 2a.1.4).

Design notes:
- Frames without ``file`` or ``line`` metadata are silently dropped.
- Paths outside the repo (stdlib, third-party, Windows system files) are
  silently dropped - the agent should only propose fixes to user code.
- Non-existent files are silently dropped (symbol pointed at a file the
  user doesn't have locally).
- Overlapping ranges inside one file are merged into a single block.
- Each block is prefixed with ``// lines LO-HI`` - renders as a harmless
  line comment in C/C++/C#/Java/Go/JS/TS/Rust and most other languages
  the fix agent might be asked to repair.
"""

from __future__ import annotations

from pathlib import Path

from debugbridge.fix.models import CallFrame

__all__ = ["extract_source_snippets"]


def _repo_relative(repo: Path, candidate: Path) -> Path | None:
    """Return ``candidate`` as a repo-relative Path, or None if it's outside the repo."""
    try:
        repo_resolved = repo.resolve()
        cand_resolved = candidate.resolve()
    except OSError:
        return None
    try:
        return cand_resolved.relative_to(repo_resolved)
    except ValueError:
        return None


def _merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping or touching inclusive ranges. Input need not be sorted."""
    if not ranges:
        return []
    sorted_ranges = sorted(ranges)
    merged: list[tuple[int, int]] = [sorted_ranges[0]]
    for lo, hi in sorted_ranges[1:]:
        prev_lo, prev_hi = merged[-1]
        if lo <= prev_hi + 1:
            merged[-1] = (prev_lo, max(prev_hi, hi))
        else:
            merged.append((lo, hi))
    return merged


def extract_source_snippets(
    repo: Path,
    callstack: list[CallFrame],
    context_lines: int = 15,
    max_files: int = 5,
) -> dict[Path, str]:
    """Return ``{repo-relative path: snippet}`` for in-repo frames with file/line.

    Each snippet concatenates one or more ``// lines LO-HI`` blocks separated by
    a blank line. Blocks within a file are merged when their plus/minus context
    ranges touch or overlap. Output is capped at ``max_files`` distinct files -
    earlier frames win (they are typically closer to the crash site).
    """
    # Accumulate ranges per repo-relative path, in the order files were first seen.
    per_file: dict[Path, list[tuple[int, int]]] = {}
    order: list[Path] = []

    for frame in callstack:
        if frame.file is None or frame.line is None:
            continue

        rel = _repo_relative(repo, Path(frame.file))
        if rel is None:
            continue

        abs_path = (repo / rel).resolve()
        if not abs_path.exists() or not abs_path.is_file():
            continue

        lo = max(1, frame.line - context_lines)
        hi = frame.line + context_lines

        if rel not in per_file:
            if len(order) >= max_files:
                continue  # Cap reached; skip new files.
            per_file[rel] = []
            order.append(rel)
        per_file[rel].append((lo, hi))

    # Render each file's snippet.
    out: dict[Path, str] = {}
    for rel in order:
        abs_path = (repo / rel).resolve()
        try:
            text = abs_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        lines = text.splitlines()
        total = len(lines)

        blocks: list[str] = []
        for lo, hi in _merge_ranges(per_file[rel]):
            clamped_hi = min(hi, total)
            header = f"// lines {lo}-{clamped_hi}"
            body = "\n".join(lines[lo - 1 : clamped_hi])
            blocks.append(f"{header}\n{body}")
        out[rel] = "\n\n".join(blocks)

    return out


# TODO(task 2a.1.4): add render_briefing(capture, snippets, build_cmd) -> str
# TODO(task 2a.1.4): add write_briefing(path, content) -> None
# TODO(task 2a.3.6): add append_retry_feedback(briefing_path, attempt_num, build_output, claude_result_text)
