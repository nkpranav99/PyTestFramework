from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logo = (By.XPATH, "//img[@alt='Website for automation practice']")

        self.login = (By.XPATH, "//a[contains(text(), ' Signup / Login')]")
        self.signup = (By.XPATH, "//a[contains(text(), ' Signup / Login')]")

        self.username = (By.XPATH, "//a[contains(text(), ''")

        self.delete_user_btn = (By.XPATH, "//a[contains(text(), ''")
        self.account_deleted_msg = (By.XPATH, "//a[contains(text(), ''")

    def get_user_name(self):
        self.driver.find_element(*self.username).text

    def delete_user(self):
        self.driver.find_element(*self.delete_user_btn).click()

    def verify_user_deletion(self):
        BasePage.wait_until_element_visible(self.account_deleted_msg)
        assert (
            self.driver.find_element(*self.account_deleted_msg).text
            == "ACCOUNT DELETED!"
        ), f"Account deletion success message does not match! Actual Message: {self.driver.find_element(*self.account_deleted_msg).text}, Expected Message: 'ACCOUNT DELETED!'"
