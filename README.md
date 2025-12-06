# AdguardFilters-Issue-Automation-Python-CLI

[![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/AdguardFilters-Issue-Automation-Python-CLI/ci.yml?style=flat-square&logo=github)](https://github.com/chirag127/AdguardFilters-Issue-Automation-Python-CLI/actions/workflows/ci.yml)
[![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/AdguardFilters-Issue-Automation-Python-CLI?style=flat-square&token=XXX)](https://codecov.io/gh/chirag127/AdguardFilters-Issue-Automation-Python-CLI)
[![License](https://img.shields.io/github/license/chirag127/AdguardFilters-Issue-Automation-Python-CLI?style=flat-square)](./LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/AdguardFilters-Issue-Automation-Python-CLI?style=flat-square&logo=github)](https://github.com/chirag127/AdguardFilters-Issue-Automation-Python-CLI)

<p align="center">
  <a href="https://stars.github.com/chirag127/AdguardFilters-Issue-Automation-Python-CLI"><img src="https://img.shields.io/badge/Star%20%E2%98%85%20this%20Repo-brightgreen?style=flat-square&logo=github" alt="Star this Repo"></a>
</p>

--- 

This repository hosts a high-performance Python CLI toolkit engineered to automate the maintenance lifecycle of large-scale content-blocking filter lists, specifically targeting issue management workflows for the `AdGuardTeam/AdguardFilters` project. It leverages structured API interaction to enhance triage efficiency and reporting accuracy.

## 🏗️ Architecture Overview (Modular Monolith)

This project follows a Modular Monolith pattern, ensuring that components—CLI interface, GitHub API abstraction, and list parsing logic—are clearly decoupled for maintainability and scalability.

ascii
AdguardFilters-Issue-Automation-Python-CLI/
├── src/
│   ├── cli/              # Command Line Interface (Click/Typer definitions)
│   ├── github_api/       # Abstraction layer for GitHub interactions (e.g., issue creation, labeling)
│   ├── core/
│   │   ├── filter_parser.py # Logic for processing filter list content (potential integration points)
│   │   └── orchestrator.py  # Business logic coordinating CLI inputs to API actions
│   └── __init__.py
├── tests/
│   ├── unit/
│   └── integration/
├── pyproject.toml        # Dependency management (uv), metadata, and build configuration
├── README.md
└── AGENTS.md             # Technical Mandates for AI Agents


## 📋 Table of Contents

1.  [Architecture Overview (Modular Monolith)](#-architecture-overview-modular-monolith)
2.  [Table of Contents](#-table-of-contents)
3.  [Key Features](#-key-features)
4.  [Apex Technical Directives (AI Agent Guidance)](#-apex-technical-directives-ai-agent-guidance)
5.  [Development & Execution](#-development--execution)
6.  [Contributing](#-contributing)
7.  [License](#-license)

## ✨ Key Features

*   **Intelligent Issue Reporting:** Programmatically create detailed bug reports based on identified filter rule failures, ensuring correct metadata tagging.
*   **Automated Triage:** Scripts to label, assign, or close stale issues based on predefined heuristics.
*   **Dependency Management (uv):** Uses modern Python tooling for fast, reproducible dependency resolution.
*   **Strict Linting:** Enforces high code quality using Ruff, adhering to PEP 8 and security best practices.

## 🤖 Apex Technical Directives (AI Agent Guidance)

<details><summary><strong>View System Mandates for Code Generation and Maintenance</strong></summary>

# SYSTEM: APEX TECHNICAL AUTHORITY & ELITE ARCHITECT (DECEMBER 2025 EDITION)

## 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

---

## 2. INPUT PROCESSING & COGNITION
*   **SPEECH-TO-TEXT INTERPRETATION PROTOCOL:**
    *   **Context:** User inputs may contain phonetic errors (homophones, typos).
    *   **Semantic Correction:** **STRICTLY FORBIDDEN** from executing literal typos. You must **INFER** technical intent based on the project context.
    *   **Logic Anchor:** Treat the `README.md` as the **Single Source of Truth (SSOT)**.
*   **MANDATORY MCP INSTRUMENTATION:**
    *   **No Guessing:** Do not hallucinate APIs. Do not use deprecated libraries.
    *   **Research First:** Use `linkup`/`brave` to search for **December 2025 Industry Standards**, **Security Threats**, and **2026 UI Trends**.
    *   **Validation:** Use `docfork` to verify *every* external API signature (especially GitHub REST/GraphQL endpoints).
    *   **Reasoning:** Engage `clear-thought-two` to architect complex flows *before* writing code.

---

## 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** Detect the project type (`pyproject.toml` for Python) and apply the corresponding **Apex Toolchain**.

*   **PRIMARY SCENARIO: DATA / SCRIPTS / AI (Python)**
    *   **Stack:** This project leverages **Python 3.12+** (latest stable requirement). Key tools include **uv** (for package management and dependency resolution), **Ruff** (for ultra-fast linting and formatting, replacing flake8/isort), and **Pytest** (for robust unit and integration testing).
    *   **Architecture:** Adheres to a **Modular Monolith** pattern, ensuring clear separation of concerns for features like GitHub API interaction, list processing, and CLI interface, while maintaining a unified deployment.
    *   **API Interfacing:** Utilize `httpx` for modern asynchronous API calls where beneficial, strictly adhering to GitHub API rate limits and best practices.
    *   **CLI Framework:** Uses `Typer` or `Click` for a powerful, intuitive, and automatically documented command-line interface.

---

## 4. ARCHITECTURAL & LINTING PRINCIPLES
*   **SOLID:** Maintain strict adherence to Single Responsibility and Interface Segregation principles, especially between the CLI layer and the core business logic.
*   **DRY:** Avoid code duplication, particularly in API error handling.
*   **YAGNI:** Implement only what is necessary for current filter automation tasks; avoid premature generalization.

## 5. VERIFICATION COMMANDS (For Automated QA)
*   **Dependency Resolution & Environment Setup:** `uv sync`
*   **Linting & Formatting Check:** `ruff check .` and `ruff format --check .`
*   **Full Test Suite Execution:** `pytest` (or `pytest --cov=src` for coverage reports)

</details>

## 🚀 Development & Execution

This project requires Python 3.12 or newer and uses `uv` for dependency management.

### Setup

1.  **Clone Repository:**
    bash
    git clone https://github.com/chirag127/AdguardFilters-Issue-Automation-Python-CLI.git
    cd AdguardFilters-Issue-Automation-Python-CLI
    

2.  **Environment Setup (Using uv):
    **
    bash
    # Create and activate a virtual environment, installing dependencies
    uv venv
    source .venv/bin/activate
    uv sync
    

### Execution Scripts

| Command | Description | Tooling Focus |
| :--- | :--- | :--- |
| `python src/cli/main.py issue create --filter-id 123` | Creates a new issue based on a filter identifier. | CLI/GitHub API |
| `pytest` | Runs all unit and integration tests. | Pytest/Ruff |
| `ruff check .` | Runs the linter to find errors and enforce style. | Ruff |
| `uv update --all` | Updates all dependencies to the latest compatible versions. | uv |

## 🤝 Contributing

We welcome contributions that enhance automation accuracy, code structure, or integrate new list maintenance heuristics. Please consult `.github/CONTRIBUTING.md` for guidelines on submission standards and PR templates.

## ⚖️ License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License**. See the [LICENSE](./LICENSE) file for full details.
