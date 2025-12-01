from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logo = (By.XPATH, "//img[@alt='Website for automation practice']")

        self.login = (By.XPATH, "//a[contains(text(), ' Signup / Login')]")
        self.signup = (By.XPATH, "//a[contains(text(), ' Signup / Login')]")

        self.logged_in_as_user = (By.XPATH, "//a[contains(text(), ' Logged in as ')]")
        self.username = (By.CSS_SELECTOR, "li a b")
        self.logout = (By.XPATH, "//a[contains(text(), ' Logout'")

        self.delete_user_btn = (By.XPATH, "//a[text()=' Delete Account']")
        self.account_deleted_msg = (By.XPATH, "//h2/b[text()='Account Deleted!']")

    def verify_logged_in_user(self):
        username = self.get_username()
        assert (
            self.driver.find_element(*self.logged_in_as_user).text
            == f"Logged in as {username}"
        ), f"Username does not match! Actual: {self.driver.find_element(*self.logged_in_as_user).text}, Expected: 'Logged in as {username}'"

    def get_username(self):
        return self.driver.find_element(*self.username).text

    def delete_user(self):
        self.driver.find_element(*self.delete_user_btn).click()

    def verify_user_deletion(self):
        BasePage.wait_until_element_visible(self, self.account_deleted_msg)
        assert (
            self.driver.find_element(*self.account_deleted_msg).text
            == "ACCOUNT DELETED!"
        ), f"Account deletion success message does not match! Actual Message: {self.driver.find_element(*self.account_deleted_msg).text}, Expected Message: 'ACCOUNT DELETED!'"
