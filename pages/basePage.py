from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click_on_element(self, element):
        try:
            self.driver.find_element(*element).click()
        except NoSuchElementException:
            self.scroll_to_element(self.driver.find_element(*element))
            self.driver.find_element(*element).click()

    def wait_until_element_visible(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((element)))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true)", element)

    def wait(self, delay):
        self.driver.implicitly_wait(delay)

