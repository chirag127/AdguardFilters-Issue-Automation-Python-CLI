# AdguardFilters-Issue-Automation-Python-CLI

[![Live](https://img.shields.io/badge/live-oriz.in-2ea44f?style=flat-square)](https://AdguardFilters-Issue-Automation-Python-CLI.oriz.in)
[![Stars](https://img.shields.io/github/stars/chirag127/AdguardFilters-Issue-Automation-Python-CLI?style=flat-square)](https://github.com/chirag127/AdguardFilters-Issue-Automation-Python-CLI/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

Python CLI that automates issue reporting and repetitive browser tasks for AdGuard filter-list maintenance — email reports, Brave Community topics, bulk commenting, auto-clicking, extension cleanup, and screenshots.

Live page: https://AdguardFilters-Issue-Automation-Python-CLI.oriz.in

---

## Features

- **Email Reporting** — generate and send ad-blocking reports via email.
- **Brave Community Reporting** — automate creating new topics on the Brave Community forum.
- **Automated Commenting** — post predefined comments across multiple tabs with one command.
- **Auto-Clicker** — replay a sequence of clicks and key presses for repetitive tasks.
- **Extension Management** — remove multiple browser extensions quickly.
- **Screenshot Utility** — capture a region or the full screen.

---

## Installation

Requires Python 3.9+.

```bash
git clone https://github.com/chirag127/AdguardFilters-Issue-Automation-Python-CLI.git
cd AdguardFilters-Issue-Automation-Python-CLI
pip install -e .
```

Copy `.env.example` to `.env` and fill in the values (SMTP creds, GitHub token, etc.).

```bash
cp .env.example .env
```

---

## Usage

```bash
python src/main.py <task>
```

`<task>` is one of:

| Task | Action |
|------|--------|
| `report-email` | Generate + send an ad-blocking report by email |
| `report-brave` | Create a new topic on the Brave Community forum |
| `post-comments` | Post predefined comments across open tabs |
| `auto-click` | Replay a click/keypress sequence |
| `remove-extensions` | Bulk-remove browser extensions |
| `screenshot` | Capture a region or full screen |

---

## Project layout

```
src/
  main.py             # CLI entry point / task dispatch
  email_reporter.py   # email report generation + send
  brave_reporter.py   # Brave Community topic automation
  comment_placer.py   # multi-tab comment posting
  auto_clicker.py     # click/keypress replay
  extension_remover.py# browser extension removal
  screenshot.py       # screen capture
  browser_utils.py    # shared browser helpers
  automation_utils.py # shared automation helpers
  file_utils.py       # file helpers
  config.py           # env/config loading
assets/               # reference images for image-matching automation
```

---

## Contributing

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

[MIT](LICENSE) © Chirag Singhal.

---

## Star this repo

If this project is useful, please consider giving it a star.
