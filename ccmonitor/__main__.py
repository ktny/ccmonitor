"""Entry point for ccmonitor."""

import click

from .timeline_monitor import TimelineMonitor


@click.command()
@click.option(
    "--days",
    default=1,
    help="Number of days to look back (default: 1)",
    type=int,
)
@click.option(
    "--project",
    help="Filter by specific project",
    type=str,
)
def main(days: int, project: str | None) -> None:
    """Claude Session Timeline - Claudeセッションの時系列可視化ツール."""
    try:
        # Note: project filtering will be implemented later
        if project:
            click.echo("Project filtering is not yet implemented")
            
        monitor = TimelineMonitor(days=days)
        monitor.run()

    except KeyboardInterrupt:
        click.echo("\n👋 Exiting.")
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)


if __name__ == "__main__":
    main()
