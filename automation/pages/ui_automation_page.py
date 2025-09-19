from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UIAutomationPage:

	# Locators (store strings only; use By.XPATH when calling driver)
	SEARCH_INPUT = '//input[@type="text"]'
	RESULT_ITEM_TITLE = '//div[@role="listitem"]//h2//span'
	RESULT_ITEM_PRICE = '//div[@role= "listitem"]//span[@class="a-price-whole"]'
	RESULT_ITEM_RATING = '//div[@role= "listitem"]//span[@class="a-icon-alt"]'
	RESULT_PRESENT = '//div[@role="listitem"]//h2//span'

	def __init__(self, driver):
		self.driver = driver

	def open(self, url: str):
		self.driver.get(url)

	def search(self, term: str, wait_timeout: int = 15):
		# use explicit By and locator strings
		self.driver.find_element(By.XPATH, self.SEARCH_INPUT).click()
		self.driver.find_element(By.XPATH, self.SEARCH_INPUT).send_keys(term)
		self.driver.switch_to.active_element.send_keys(Keys.ENTER)
		WebDriverWait(self.driver, wait_timeout).until(
			EC.presence_of_element_located((By.XPATH, self.RESULT_PRESENT))
		)
		

	def get_mobile_rows(self):
		names = self.driver.find_elements(By.XPATH, self.RESULT_ITEM_TITLE)
		prices = self.driver.find_elements(By.XPATH, self.RESULT_ITEM_PRICE)
		ratings = self.driver.find_elements(By.XPATH, self.RESULT_ITEM_RATING)
		rows = []
		count = min(len(names), len(prices), len(ratings))
		for i in range(count):
			rows.append({
				'name': names[i].text.strip(),
				'price': prices[i].text.strip(),
				'rating': ratings[i].text.strip(),
			})
		return rows
