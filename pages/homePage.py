from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logo = (By.XPATH, "//img[@alt='Website for automation practice']")

        self.login = (By.XPATH, "//a[contains(text(), ' Signup / Login')]")
        self.signup = (By.XPATH, "//a[contains(text(), ' Signup / Login')]")



