"""Typer CLI for DebugBridge.

Kept intentionally free of pybag / session imports at module load time so that
``debugbridge doctor`` and ``debugbridge version`` work on a machine without
Windows Debugging Tools installed. The server is only imported inside ``serve``.
"""

from __future__ import annotations

import sys

import typer
from rich.console import Console
from rich.table import Table

from debugbridge import __version__
from debugbridge.env import check_debugging_tools

app = typer.Typer(
    name="debugbridge",
    help="Remote crash capture MCP server for native Windows applications.",
    add_completion=False,
    no_args_is_help=True,
)

console = Console()


@app.command()
def serve(
    transport: str = typer.Option(
        "http",
        "--transport",
        "-t",
        help='Transport: "http" (Streamable HTTP, recommended) or "stdio".',
    ),
    host: str = typer.Option("127.0.0.1", "--host", help="Bind host for HTTP transport."),
    port: int = typer.Option(8585, "--port", "-p", help="Bind port for HTTP transport."),
    skip_env_check: bool = typer.Option(
        False, "--skip-env-check", help="Start even if Debugging Tools look absent (debug use)."
    ),
) -> None:
    """Start the DebugBridge MCP server."""
    if transport not in ("http", "stdio"):
        console.print(f"[red]Invalid transport: {transport}. Use 'http' or 'stdio'.[/red]")
        raise typer.Exit(code=2)

    if not skip_env_check:
        result = check_debugging_tools()
        if not result.ok:
            console.print("[red]Windows Debugging Tools not found.[/red]\n")
            console.print(result.guidance or "")
            console.print(
                "\nRe-run with --skip-env-check to start anyway (server will fail on first attach)."
            )
            raise typer.Exit(code=1)

    # Deferred import — loads pybag, which requires dbgeng.dll.
    from debugbridge.server import run

    if transport == "http":
        console.print(
            f"[green]DebugBridge[/green] serving on [bold]http://{host}:{port}/mcp[/bold]"
        )
    else:
        console.print("[green]DebugBridge[/green] serving on stdio")
    run(transport=transport, host=host, port=port)  # type: ignore[arg-type]


@app.command()
def doctor() -> None:
    """Check that Windows Debugging Tools are installed and findable."""
    result = check_debugging_tools()

    table = Table(title="DebugBridge environment check", show_header=True)
    table.add_column("Component")
    table.add_column("Status")
    table.add_column("Path")

    all_items = sorted({*result.found.keys(), *result.missing})
    for name in all_items:
        if name in result.found:
            table.add_row(name, "[green]found[/green]", result.found[name])
        else:
            table.add_row(name, "[red]missing[/red]", "—")

    console.print(table)

    if result.ok:
        console.print("\n[green]All required Debugging Tools are present.[/green]")
        raise typer.Exit(code=0)

    console.print(f"\n[yellow]Missing: {', '.join(result.missing)}[/yellow]\n")
    console.print(result.guidance or "")
    raise typer.Exit(code=1)


@app.command()
def version() -> None:
    """Print DebugBridge's version and exit."""
    console.print(f"debugbridge {__version__}")


def main() -> None:
    """Entry point wrapper — lets us set exit codes consistently."""
    try:
        app()
    except typer.Exit:
        raise
    except Exception as e:  # pragma: no cover — top-level safety net
        console.print(f"[red]Fatal:[/red] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
