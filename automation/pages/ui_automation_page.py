from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class UIAutomationPage:

	SEARCH_INPUT = '//input[@type="text"]'
	RESULT_ITEM_TITLE = '//div[@role="listitem"]//h2//span'
	RESULT_ITEM_PRICE = '//div[@role= "listitem"]//span[@class="a-price-whole"]'
	RESULT_ITEM_RATING = '//div[@role= "listitem"]//span[@class="a-icon-alt"]'
	RESULT_ITEM_REVIEWS = '//div[@role= "listitem"]//span[contains(@class,"s-underline-text")]'
	RESULT_PRESENT = '//div[@role="listitem"]//h2//span'

	def __init__(self, driver):
		self.driver = driver

	def open(self, url: str):
		self.driver.get(url)
		logger.info(f"Opened URL: {url}")

	def search(self, term: str, wait_timeout: int = 15):
		logger.info(f"Initiating search for term: {term}")
		self.driver.find_element(By.XPATH, self.SEARCH_INPUT).click()
		self.driver.find_element(By.XPATH, self.SEARCH_INPUT).send_keys(term)
		self.driver.switch_to.active_element.send_keys(Keys.ENTER)
		WebDriverWait(self.driver, wait_timeout).until(EC.presence_of_element_located((By.XPATH, self.RESULT_PRESENT)))
		logger.info(f"Searched for term: {term}")


	def get_mobile_rows(self):
		logger.info("Extracting mobile rows from search results")
		names = self.driver.find_elements(By.XPATH, self.RESULT_ITEM_TITLE)
		prices = self.driver.find_elements(By.XPATH, self.RESULT_ITEM_PRICE)
		ratings = self.driver.find_elements(By.XPATH, self.RESULT_ITEM_RATING)
		reviews = self.driver.find_elements(By.XPATH, self.RESULT_ITEM_REVIEWS)
		rows = []
		count = min(len(names), len(prices), len(ratings), len(reviews))
		logger.info(f"Found {count} complete result rows")
		for i in range(count):
			rows.append({
				'Name': names[i].text.strip(),
				'Price': prices[i].text.strip(),
				'Rating': ratings[i].get_attribute("textContent")[:3].strip(),
				'Reviews': reviews[i].get_attribute("textContent").strip()
			})
		logger.info(f"Extracted {len(rows)} rows of mobile data with name, price, rating, and reviews")
		return rows
