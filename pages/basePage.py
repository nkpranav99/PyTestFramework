from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    def wait_until_element_visible(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((element)))
