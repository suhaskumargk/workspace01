import pytest

from automation.utils.config_manager import ConfigManager
from automation.utils.Excel_reader import save_table
from automation.pages.ui_automation_page import UIAutomationPage
import logging
import allure

logger = logging.getLogger(__name__)


class Test_UI_Automation:

    @allure.title("Test create user")
    @allure.description("This test attempts to create a user in the system.")
    @allure.testcase("TESTCASE-001")
    @pytest.mark.ui
    def test_open_base_url(self, driver):
        cm = ConfigManager()
        page = UIAutomationPage(driver)
        page.open(cm.get('production_env', 'base_urls'))
        logger.info(f"Test navigated to URL: {driver.current_url}")
        page.search('Mobile')
        rows = page.get_mobile_rows()
        assert len(rows) >= 10, f"Expected at least 10 result rows, but found {len(rows)}"
        save_table(rows, 'automation/reports/mobiles.csv')
        save_table(rows, 'automation/reports/mobiles.xlsx')