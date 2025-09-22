import pytest
from automation.pages.ui_automation_page import UIAutomationPage
from automation.utils.config_manager import ConfigManager
from automation.utils.Excel_reader import save_table
import logging
import allure

logger = logging.getLogger(__name__)


class Test_UI_Automation:

    @allure.title("Test to search items and save results to Excel")
    @allure.description("This test searches for mobile items and saves the results to an Excel file.")
    @allure.testcase("TESTCASE-001")
    @pytest.mark.ui
    def test_open_base_url(self, driver):
        """Test to open base URL and verify the data for searched items."""
        page = UIAutomationPage(driver)
        env = ConfigManager.get('production_env', 'base_url')
        page.open(env)
        page.search('Mobile')
        rows = page.get_mobile_rows()
        assert len(rows) > 0, f"Expected at least 1 result rows, but found {len(rows)}"
        save_table(rows, 'automation/reports/mobiles.xlsx')
        logger.info(f"Saved {len(rows)} rows of mobile data to Excel file")