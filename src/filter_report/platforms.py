"""Per-platform registry for filter-report."""

from dataclasses import dataclass, field


@dataclass
class Platform:
    id: str
    name: str
    repo: str  # "owner/repo" for GitHub, URL otherwise
    issue_type: str  # "github_issues" | "github_discussions" | "web_form"
    base_url: str
    template: str | None = None
    notes: str = ""
    # GitHub query-param keys differ by platform
    accepts_categories: list = field(default_factory=list)


PLATFORMS: dict[str, Platform] = {
    "uassets": Platform(
        id="uassets",
        name="uBlock uAssets",
        repo="uBlockOrigin/uAssets",
        issue_type="github_issues",
        base_url="https://github.com/uBlockOrigin/uAssets/issues/new",
        template="",
        notes="Requires prerequisite checkboxes; pre-fill title+body only.",
        accepts_categories=[
            "ad",
            "tracker",
            "cookie-popup",
            "annoyance",
            "social-share",
        ],
    ),
    "adguard": Platform(
        id="adguard",
        name="AdGuard Filters",
        repo="AdguardTeam/AdguardFilters",
        issue_type="github_issues",
        base_url="https://github.com/AdguardTeam/AdguardFilters/issues/new",
        template="",
        notes="AdGuard issue tracker; pick correct category in title.",
        accepts_categories=[
            "ad",
            "tracker",
            "cookie-popup",
            "annoyance",
            "social-share",
            "newsletter-popup",
            "paywall",
        ],
    ),
    "easylist": Platform(
        id="easylist",
        name="EasyList",
        repo="easylist/easylist",
        issue_type="github_issues",
        base_url="https://github.com/easylist/easylist/issues/new",
        template="",
        notes="EasyList and Fanboy Annoyances share this tracker.",
        accepts_categories=["ad", "tracker", "annoyance"],
    ),
    "fanboy": Platform(
        id="fanboy",
        name="Fanboy Annoyances",
        repo="easylist/easylist",
        issue_type="github_issues",
        base_url="https://github.com/easylist/easylist/issues/new",
        template="",
        notes="Fanboy lists are maintained via the EasyList issue tracker.",
        accepts_categories=[
            "cookie-popup",
            "annoyance",
            "social-share",
            "newsletter-popup",
        ],
    ),
    "brave": Platform(
        id="brave",
        name="Brave adblock-lists",
        repo="brave/adblock-lists",
        issue_type="github_issues",
        base_url="https://github.com/brave/adblock-lists/issues/new",
        template="",
        notes="Brave browser default filter list.",
        accepts_categories=["ad", "tracker", "annoyance"],
    ),
    "adfilt": Platform(
        id="adfilt",
        name="DandelionSprout/adfilt",
        repo="DandelionSprout/adfilt",
        issue_type="github_discussions",
        base_url="https://github.com/DandelionSprout/adfilt/discussions/new",
        template="",
        notes="Uses GitHub Discussions, not Issues. Select category after opening.",
        accepts_categories=[
            "ad",
            "tracker",
            "cookie-popup",
            "annoyance",
            "social-share",
            "newsletter-popup",
        ],
    ),
    "peterlowe": Platform(
        id="peterlowe",
        name="Peter Lowe's List",
        repo="",
        issue_type="web_form",
        base_url="https://pgl.yoyo.org/adservers/report.php",
        notes="Web form — browser will open the report page.",
        accepts_categories=["ad", "tracker"],
    ),
    "ph00lt0": Platform(
        id="ph00lt0",
        name="ph00lt0/blocklist",
        repo="ph00lt0/blocklist",
        issue_type="github_issues",
        base_url="https://github.com/ph00lt0/blocklist/issues/new",
        template="",
        notes="Community blocklist.",
        accepts_categories=["ad", "tracker", "annoyance"],
    ),
}

CATEGORIES = [
    "ad",
    "tracker",
    "cookie-popup",
    "social-share",
    "newsletter-popup",
    "annoyance",
    "paywall",
]
