"""CLI entry point for filter-report."""

from __future__ import annotations

import webbrowser

import click

from .platforms import CATEGORIES, PLATFORMS
from .report import build_reports


def _parse_platforms(platforms_str: str) -> list[str]:
    ids = [p.strip() for p in platforms_str.split(",") if p.strip()]
    unknown = [p for p in ids if p not in PLATFORMS]
    if unknown:
        raise click.BadParameter(
            f"Unknown platform(s): {', '.join(unknown)}. "
            f"Run `filter-report platforms` for valid IDs."
        )
    return ids


@click.group()
@click.version_option(package_name="filter-report")
def cli():
    """Multi-platform ad/annoyance filter report preparer.

    Builds pre-filled GitHub issue URLs and opens them in your browser
    for 1-click human submit. Does NOT auto-file issues (filter-list
    projects require human reporters; bots get banned).
    """


@cli.command()
@click.argument("url")
@click.option(
    "--category",
    "-c",
    required=True,
    type=click.Choice(CATEGORIES),
    help="Type of annoyance being reported.",
)
@click.option(
    "--platforms",
    "-p",
    default="uassets,adguard",
    show_default=True,
    help="Comma-separated platform IDs. Run `filter-report platforms` for list.",
)
@click.option("--selector", "-s", default=None, help="CSS selector for the element.")
@click.option(
    "--screenshot",
    default=None,
    help="Public URL or local path to screenshot (added to body as-is).",
)
@click.option(
    "--no-browser",
    is_flag=True,
    default=False,
    help="Print URLs without opening browser.",
)
def prepare(url, category, platforms, selector, screenshot, no_browser):
    """Prepare reports for URL and open pre-filled issue pages.

    Example:

        filter-report prepare https://example.com --category cookie-popup
        filter-report prepare https://example.com -c ad -p uassets,adguard,easylist
    """
    platform_ids = _parse_platforms(platforms)
    reports = build_reports(url, category, platform_ids, selector, screenshot)

    click.echo(f"\nPrepared {len(reports)} report(s) for: {url}\n")
    for r in reports:
        click.echo(f"  [{r['platform_name']}]  ({r['issue_type']})")
        click.echo(f"  Title : {r['title']}")
        click.echo(
            f"  URL   : {r['open_url'][:120]}{'...' if len(r['open_url']) > 120 else ''}"
        )
        click.echo()

    if not no_browser:
        click.echo("Opening in browser — review and click Submit.\n")
        for r in reports:
            webbrowser.open(r["open_url"])
    else:
        click.echo("--no-browser set; copy URLs above to submit.")


@cli.command()
def platforms():
    """List all supported platforms and their IDs."""
    click.echo(f"\n{'ID':<12} {'Name':<30} {'Type':<20} {'Categories'}")
    click.echo("-" * 90)
    for pid, p in PLATFORMS.items():
        cats = ", ".join(p.accepts_categories) if p.accepts_categories else "all"
        click.echo(f"{pid:<12} {p.name:<30} {p.issue_type:<20} {cats}")
    click.echo()


@cli.command()
@click.argument("domain")
@click.option(
    "--type",
    "rule_type",
    type=click.Choice(["block", "hide", "block-csp"]),
    default="block",
    show_default=True,
    help="Rule type to generate.",
)
def rule(domain, rule_type):
    """Generate an adblock-syntax rule for DOMAIN.

    Examples:

        filter-report rule ads.example.com
        filter-report rule banner.example.com --type hide
    """
    domain = domain.strip().lstrip("https://").lstrip("http://").split("/")[0]
    if rule_type == "block":
        click.echo(f"||{domain}^")
    elif rule_type == "hide":
        click.echo(f"##.{domain}")
        click.echo("\n# More likely you want a CSS selector. Generic example:")
        click.echo("example.com##.ad-banner")
    elif rule_type == "block-csp":
        click.echo(f"||{domain}^$csp=script-src 'none'")


def main():
    cli()


if __name__ == "__main__":
    main()
