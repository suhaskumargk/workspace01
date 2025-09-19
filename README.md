# Automation Framework

This repository contains a modular pytest-based automation framework and
example UI/API tests.

Setup instructions
------------------

1. Create and activate a Python virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r automation/requirements.txt
```

How to run UI tests
-------------------

Run only UI-marked tests and show console output (use -s to disable capture):

```bash
pytest -m ui 
```

How to run API tests
--------------------

Run API-marked tests (example):

```bash
pytest -m api
```

How to generate / view reports
------------------------------

To produce a self-contained HTML report (requires `pytest-html`):

```bash
pytest --html=automation/reports/report.html --self-contained-html
```

Open `automation/reports/report.html` in your browser to view the
report.

Alternatively, you can generate an Allure report (recommended for
richer test-results visualization). Run the tests with the Allure
results directory and then serve the report locally:

```bash
pytest --alluredir=allure-results
allure serve allure-results/
```

Notes:
- Install `pytest-html` to use the `--html` option: `pip install pytest-html`.
- For Allure, install `allure-pytest` (`pip install allure-pytest`) and
  the Allure commandline tool (install via package manager or from
  https://docs.qameta.io/allure/).

Framework structure
-------------------

This repository follows a modular automation framework layout. The core
folders you should expect under `automation/` are:

```
automation/
├── tests/                 # test suites
│   ├── ui/                # UI tests
│   ├── api/               # API tests
├── pages/                 # Page Object Models for UI automation
├── utils/                 # helpers (Excel reader, config manager, logger, common methods)
├── configs/               # environment/config files (JSON/YAML/INI)
├── reports/               # generated reports and logs
├── requirements.txt       # Python dependencies
└── README.md
```

Requirements
------------

- Config-driven: base URLs, browser, and environment settings are stored
  under `configs/` and loaded by the config manager.
- Reusable utilities: `utils/` should contain the Excel/CSV reader,
  logger, API client wrapper and other helpers so tests remain DRY.
- Support multiple environments: dev/uat/prod support with environment
  specific configuration and credential files.

Notes
-----

- Register any custom pytest marks (like `api` and `ui`) in `pytest.ini` to
  avoid warnings. Example:

```ini
[pytest]
markers =
    api: mark tests as API tests
    ui: mark tests as UI tests
```

- Scraping live pages can be flaky due to network conditions, dynamic
  page changes, or anti-bot measures; consider adding retries, explicit
  waits, or using a headless browser profile for CI runs.
