# filter-report

[![Live](https://img.shields.io/badge/live-filter--report.oriz.in-blue)](https://filter-report.oriz.in)
[![Stars](https://img.shields.io/github/stars/chirag127/filter-report?style=social)](https://github.com/chirag127/filter-report/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/filter-report)](https://pypi.org/project/filter-report/)

**Multi-platform ad/tracker/cookie-popup/annoyance filter report preparer.**

Builds pre-filled GitHub issue URLs for uBlock uAssets, AdGuard Filters, EasyList, Brave, DandelionSprout/adfilt, and more — then opens them in your browser for **1-click human submit**.

Live site: **https://filter-report.oriz.in**

---

## Why semi-automatic, not headless?

Every major filter-list project (uBlock, AdGuard, EasyList, Brave) explicitly **requires human reporters**. Automated/bot issue creation leads to bans and revoked access. This tool does the tedious part (formatting the correct template, filling title/body, constructing the URL) and leaves the actual Submit click to you. That 1-click is intentional — it is the only policy-compliant design.

---

## Supported platforms

| ID         | Name                    | Type                | Accepted categories                                         |
|------------|-------------------------|---------------------|-------------------------------------------------------------|
| `uassets`  | uBlock uAssets          | GitHub Issues       | ad, tracker, cookie-popup, annoyance, social-share          |
| `adguard`  | AdGuard Filters         | GitHub Issues       | ad, tracker, cookie-popup, annoyance, social-share, newsletter-popup, paywall |
| `easylist` | EasyList                | GitHub Issues       | ad, tracker, annoyance                                      |
| `fanboy`   | Fanboy Annoyances       | GitHub Issues (EasyList tracker) | cookie-popup, annoyance, social-share, newsletter-popup |
| `brave`    | Brave adblock-lists     | GitHub Issues       | ad, tracker, annoyance                                      |
| `adfilt`   | DandelionSprout/adfilt  | GitHub Discussions  | ad, tracker, cookie-popup, annoyance, social-share, newsletter-popup |
| `peterlowe`| Peter Lowe's List       | Web form            | ad, tracker                                                 |
| `ph00lt0`  | ph00lt0/blocklist       | GitHub Issues       | ad, tracker, annoyance                                      |

---

## Install

```bash
pip install filter-report
```

Or from source:

```bash
pip install -e .
```

---

## Usage

### Prepare reports and open in browser

```bash
# Cookie popup on example.com → uBlock + AdGuard (default)
filter-report prepare https://example.com --category cookie-popup

# Ad on example.com → three platforms
filter-report prepare https://example.com -c ad -p uassets,adguard,easylist

# With CSS selector, no browser (print URLs only)
filter-report prepare https://example.com -c tracker \
  --selector "#tracker-pixel" \
  --no-browser

# All annoyances platforms
filter-report prepare https://example.com -c annoyance \
  -p uassets,adguard,easylist,fanboy,brave,adfilt,ph00lt0
```

### List platforms

```bash
filter-report platforms
```

### Generate an adblock rule

```bash
filter-report rule ads.example.com
# => ||ads.example.com^

filter-report rule banner.example.com --type hide
# => ##.banner.example.com
```

---

## Categories

| ID                | Description                        |
|-------------------|------------------------------------|
| `ad`              | Advertisement / ad element         |
| `tracker`         | Tracker / analytics script         |
| `cookie-popup`    | Cookie consent popup / GDPR banner |
| `social-share`    | Social share / like button widget  |
| `newsletter-popup`| Newsletter / email capture popup   |
| `annoyance`       | General annoyance                  |
| `paywall`         | Soft paywall / ad-block detector   |

---

## How it works

1. `filter-report prepare <url> --category <cat> --platforms <ids>` builds the correct issue title + body for each platform using GitHub's `?title=...&body=...` query-param pre-fill.
2. Each URL is opened in your default browser — one tab per platform.
3. You review the pre-filled form and click **Submit**. Done.

No credentials required. No GitHub token. No API calls. Pure URL construction.

---

## License

MIT — see [LICENSE](LICENSE).
