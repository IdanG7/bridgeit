"""Tests for fix/briefing.py source-snippet extractor (task 2a.1.3).

The briefing *renderer* itself (render_briefing) lands in task 2a.1.4.
"""

from __future__ import annotations

from pathlib import Path

from debugbridge.fix.briefing import extract_source_snippets
from debugbridge.models import CallFrame


def _frame(file: str | None, line: int | None, function: str = "f") -> CallFrame:
    """Minimal CallFrame factory for tests."""
    return CallFrame(
        index=0,
        function=function,
        module="m",
        file=file,
        line=line,
        instruction_pointer=0,
    )


def test_extract_returns_empty_when_no_frames(tmp_path: Path) -> None:
    result = extract_source_snippets(tmp_path, callstack=[])
    assert result == {}


def test_extract_skips_frames_without_file_or_line(tmp_path: Path) -> None:
    result = extract_source_snippets(
        tmp_path,
        callstack=[
            _frame(file=None, line=42),
            _frame(file="x.cpp", line=None),
        ],
    )
    assert result == {}


def test_extract_skips_files_outside_repo(tmp_path: Path) -> None:
    # Make a file OUTSIDE the repo
    outside = tmp_path.parent / "outside.cpp"
    outside.write_text("\n".join(f"line{i}" for i in range(1, 60)), encoding="utf-8")
    try:
        result = extract_source_snippets(
            tmp_path,
            callstack=[_frame(file=str(outside), line=10)],
        )
        assert result == {}
    finally:
        outside.unlink(missing_ok=True)


def test_extract_skips_nonexistent_files(tmp_path: Path) -> None:
    # Path is inside repo but file doesn't exist.
    ghost = tmp_path / "ghost.cpp"
    assert not ghost.exists()
    result = extract_source_snippets(
        tmp_path,
        callstack=[_frame(file=str(ghost), line=10)],
    )
    assert result == {}


def test_extract_returns_snippet_for_in_repo_frame(tmp_path: Path) -> None:
    src = tmp_path / "crash.cpp"
    src.write_text("\n".join(f"line{i}" for i in range(1, 101)), encoding="utf-8")

    result = extract_source_snippets(
        tmp_path,
        callstack=[_frame(file=str(src), line=40)],
        context_lines=5,
    )
    assert len(result) == 1
    key = next(iter(result))
    assert key.name == "crash.cpp"
    snippet = result[key]
    # Must start with a `// lines LO-HI` marker.
    first_line = snippet.splitlines()[0]
    assert first_line.startswith("// lines ")
    # line40 ± 5 = lines 35..45 inclusive.
    assert "line35" in snippet
    assert "line40" in snippet
    assert "line45" in snippet
    assert "line34" not in snippet
    assert "line46" not in snippet


def test_extract_merges_overlapping_ranges_in_same_file(tmp_path: Path) -> None:
    """Two frames in the same file at lines 40 and 45 with context=10 -> one merged range (30..55)."""
    src = tmp_path / "crash.cpp"
    src.write_text("\n".join(f"line{i}" for i in range(1, 101)), encoding="utf-8")

    result = extract_source_snippets(
        tmp_path,
        callstack=[
            _frame(file=str(src), line=40),
            _frame(file=str(src), line=45),
        ],
        context_lines=10,
    )
    assert len(result) == 1
    snippet = next(iter(result.values()))
    # Exactly one "// lines " header - not two.
    headers = [ln for ln in snippet.splitlines() if ln.startswith("// lines ")]
    assert len(headers) == 1
    # Merged range 30..55 inclusive.
    assert "30" in headers[0]
    assert "55" in headers[0]
    assert "line30" in snippet
    assert "line55" in snippet


def test_extract_keeps_non_overlapping_ranges_separate_within_one_file(tmp_path: Path) -> None:
    """Frames at lines 10 and 80 with context=5 -> two separate `// lines` blocks in one file."""
    src = tmp_path / "crash.cpp"
    src.write_text("\n".join(f"line{i}" for i in range(1, 101)), encoding="utf-8")

    result = extract_source_snippets(
        tmp_path,
        callstack=[
            _frame(file=str(src), line=10),
            _frame(file=str(src), line=80),
        ],
        context_lines=5,
    )
    assert len(result) == 1
    snippet = next(iter(result.values()))
    headers = [ln for ln in snippet.splitlines() if ln.startswith("// lines ")]
    assert len(headers) == 2


def test_extract_respects_max_files_cap(tmp_path: Path) -> None:
    """When stack has 10 in-repo frames spanning 10 distinct files, result cap applies."""
    frames = []
    for i in range(10):
        src = tmp_path / f"file{i}.cpp"
        src.write_text(f"content of file{i}\n", encoding="utf-8")
        frames.append(_frame(file=str(src), line=1))
    result = extract_source_snippets(tmp_path, callstack=frames, max_files=3)
    assert len(result) == 3


def test_extract_resolves_absolute_and_relative_paths(tmp_path: Path) -> None:
    """Absolute path to in-repo file -> resolved relative-to-repo key."""
    sub = tmp_path / "src"
    sub.mkdir()
    src = sub / "crash.cpp"
    src.write_text("\n".join(f"L{i}" for i in range(1, 10)), encoding="utf-8")

    # Pass an absolute path
    result = extract_source_snippets(
        tmp_path,
        callstack=[_frame(file=str(src.resolve()), line=5)],
        context_lines=2,
    )
    assert len(result) == 1
    key = next(iter(result))
    # Key is repo-relative
    assert key == Path("src/crash.cpp") or key == Path("src") / "crash.cpp"
