"""Build pre-filled issue URLs and report bodies for each platform."""

from __future__ import annotations

import urllib.parse

from .platforms import PLATFORMS, Platform

CATEGORY_LABELS = {
    "ad": "Advertisement / Ad element",
    "tracker": "Tracker / Analytics script",
    "cookie-popup": "Cookie consent popup / GDPR banner",
    "social-share": "Social share / Like button widget",
    "newsletter-popup": "Newsletter / email capture popup",
    "annoyance": "General annoyance",
    "paywall": "Soft paywall / ad-block detector",
}


def _issue_title(url: str, category: str) -> str:
    label = CATEGORY_LABELS.get(category, category)
    domain = urllib.parse.urlparse(url).netloc or url
    return f"[{label}] {domain}"


def _issue_body(
    url: str,
    category: str,
    selector: str | None,
    screenshot: str | None,
    platform_notes: str,
) -> str:
    label = CATEGORY_LABELS.get(category, category)
    lines = [
        "## Problem description",
        "",
        f"**URL:** {url}",
        f"**Category:** {label}",
        "",
    ]
    if selector:
        lines += [f"**Element selector:** `{selector}`", ""]
    if screenshot:
        lines += [f"**Screenshot:** {screenshot}", ""]
    lines += [
        "## Steps to reproduce",
        "",
        "1. Open the URL above.",
        "2. Observe the element/behaviour described.",
        "",
        "## Expected behaviour",
        "",
        "Element/script should be blocked or hidden.",
        "",
        "## Additional context",
        "",
        "_Report prepared by [filter-report](https://filter-report.oriz.in). "
        "Submitted by a human reviewer._",
    ]
    if platform_notes:
        lines += ["", f"> Note: {platform_notes}"]
    return "\n".join(lines)


def _uassets_body(url: str, category: str, selector: str | None) -> str:
    """uAssets has a specific template format."""
    label = CATEGORY_LABELS.get(category, category)
    domain = urllib.parse.urlparse(url).netloc or url
    lines = [
        "<!--",
        "  Please complete the checklist below before submitting.",
        "  Remove items that are not applicable.",
        "-->",
        "",
        "### Checklist",
        "",
        "- [ ] I have read the [documentation](https://github.com/uBlockOrigin/uAssets/blob/master/CONTRIBUTING.md)",
        "- [ ] I have verified the issue is reproducible with only uBlock Origin enabled",
        "- [ ] I have searched for existing issues",
        "",
        "### Problem description",
        "",
        f"**URL:** {url}",
        f"**Category:** {label}",
        f"**Domain:** {domain}",
        "",
    ]
    if selector:
        lines += [f"**Element selector:** `{selector}`", ""]
    lines += [
        "### Expected behaviour",
        "",
        "Element should be blocked or hidden by the filter list.",
        "",
        "_Report prepared by [filter-report](https://filter-report.oriz.in). Human reviewer submitting._",
    ]
    return "\n".join(lines)


def build_report(
    url: str,
    category: str,
    platform_id: str,
    selector: str | None = None,
    screenshot: str | None = None,
) -> dict:
    """Return dict with title, body, open_url for a single platform."""
    p: Platform = PLATFORMS[platform_id]
    title = _issue_title(url, category)

    if platform_id == "uassets":
        body = _uassets_body(url, category, selector)
    else:
        body = _issue_body(url, category, selector, screenshot, p.notes)

    if p.issue_type == "web_form":
        # Peter Lowe form — just pass domain
        domain = urllib.parse.urlparse(url).netloc or url
        params = {"site": domain}
        open_url = p.base_url + "?" + urllib.parse.urlencode(params)
    elif p.issue_type == "github_discussions":
        params = {"title": title, "body": body, "category": "General"}
        open_url = p.base_url + "?" + urllib.parse.urlencode(params)
    else:
        # github_issues
        params: dict = {"title": title, "body": body}
        if p.template:
            params["template"] = p.template
        open_url = p.base_url + "?" + urllib.parse.urlencode(params)

    return {
        "platform_id": platform_id,
        "platform_name": p.name,
        "title": title,
        "body": body,
        "open_url": open_url,
        "issue_type": p.issue_type,
    }


def build_reports(
    url: str,
    category: str,
    platform_ids: list[str],
    selector: str | None = None,
    screenshot: str | None = None,
) -> list[dict]:
    return [
        build_report(url, category, pid, selector, screenshot) for pid in platform_ids
    ]
