Pytest automation framework
===========================

This repository contains a modular pytest-based automation framework. The
project is organized to keep UI, API and feature tests separate while
providing reusable utilities for configuration, data handling and reporting.

Project layout
--------------

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

Key features / Requirements
---------------------------

- Config-driven
	- Base URLs, browser choice, and environment-specific settings are
		stored in the `configs/` folder and loaded at runtime by the config
		manager.

- Reusable utilities
	- `utils/` provides common helpers: Excel/CSV reader, config manager,
		logger, API client wrapper and other small utilities so tests stay
		concise and DRY.

- Multiple environment support
	- The framework supports different environments (dev/uat/prod). Tests
		read the active environment from configs or an environment variable
		and apply the appropriate base URL and credentials.

How to run
----------

1. Install dependencies:

```bash
pip install -r automation/requirements.txt
```

2. Run tests (example - run api tests and show output):

```bash
pytest -m api
pytest -m ui
```

3. Configure environments

- Put environment-specific settings in `automation/configs/` (for example
	`dev.json`, `uat.json`, `prod.json`) and load them via the config
	manager utility.

Notes
-----
- Register any custom pytest marks (like `api` and `ui`) in `pytest.ini`
	to avoid warnings:

```ini
[pytest]
markers =
		api: mark tests as API tests
		ui: mark tests as UI tests
```

If you'd like, I can also add a short example showing how to read
credentials from `automation/data/userdata.xlsx` using the existing utility
or add a sample `pytest.ini` and a tiny script to pick the environment at
runtime.

UI Automation (Amazon)
-----------------------

This repository includes an example UI automation test that scrapes
product data from Amazon India and saves it to CSV/XLSX. The test follows
these steps:

1. Navigate to https://www.amazon.in/
2. Search for the keyword "mobile"
3. Fetch product details from the first 2 pages (where available):
	- Mobile title
	- Price
	- Rating (if available)
	- Number of reviews (if available)
4. Save the extracted data into `automation/reports/mobiles.csv` and
	`automation/reports/mobiles.xlsx` (the project already includes a
	reusable `save_table` helper in `utils/`)
5. Validation: the test asserts that at least 10 products were scraped.

Run the UI test with:

```bash
pytest -m ui
```

Notes:
- The UI test uses Selenium and the project's page object in
  `pages/ui_automation_page.py` which includes locators for title, price
  and rating; results are collected and written using `utils/Excel_reader.py`.
- Scraping live pages can be flaky due to network conditions, dynamic
  page changes or anti-bot measures; consider adding retries, explicit
  waits, or using a headless browser profile for CI runs.

API Automation (CRUD on Users) — Completed
----------------------------------------

The API automation suite performs CRUD operations against the DummyJSON
Users API. Implementation details:

1. An Excel file with 5–10 dummy users is prepared in `automation/data/`.
2. Tests implemented:
	- Create User: read users from Excel and POST to `/users/add`.
	- Update User: modify phone/email for at least one user and PUT.
	- Get User: verify created user exists via GET.
	- Delete User: remove a user and validate deletion.

Status: Completed.

Run the API tests with the project's configured pytest command:

```bash
pytest -m api
```

Reporting
---------

Pytest HTML reporting is integrated using the `pytest-html` plugin. To
generate a self-contained HTML report run:

```bash
pytest --html=automation/reports/pytest_report.html --self-contained-html
```

The generated report will be written to `automation/reports/pytest_report.html`.

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

```bash
- To produce a self-contained HTML report using `pytest-html`:

```bash
pytest --html=automation/reports/pytest_report.html --self-contained-html
```

- After running the above command open `automation/reports/pytest_report.html` in your browser to view the report.





