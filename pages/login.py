from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.login_email = (By.XPATH, "//input[@name='email']")
        self.login_password = (By.XPATH, "//input[@name='password']")
        self.login_submit = (By.XPATH, "//button[@data-qa='login-button']")

        self.signup_username = (By.XPATH, "//input[@data-qa='signup-name']")
        self.signup_email = (By.XPATH, "//input[@data-qa='signup-email']")
        self.signup_btn = (By.XPATH, "//button[@data-qa='signup-button']")

        self.login_banner = (By.XPATH, "//h2[contains(text(), 'Login to your account')]")

    def login(self, email, password):
        self.driver.find_element(*self.login_email).send_keys(email)
        self.driver.find_element(*self.login_password).send_keys(password)
        self.driver.find_element(*self.login_submit).click()

    def register(self, name, email):
        self.driver.find_element(*self.signup_username).send_keys(name)
        self.driver.find_element(*self.signup_email).send_keys(email)
        self.driver.find_element(*self.signup_btn).click()
