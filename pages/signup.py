import json
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.basePage import BasePage



class SignUpPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

        self.acc_info_heading = (By.XPATH, "//b[text()='Enter Account Information']")
        self.title = (By.XPATH, "//input[@value='{}']")
        self.password = (By.XPATH, "//input[@name='password']")
        self.dob_day = (By.ID, "days")
        self.dob_month = (By.ID, "months")
        self.dob_year = (By.ID, "years")

        self.newsletter_signup = (By.ID, "newsletter")
        self.optin = (By.ID, "optin")

        self.first_name = (By.ID, "first_name")
        self.last_name = (By.ID, "last_name")
        self.company = (By.ID, "company")

        self.address1 = (By.ID, "address1")
        self.address2 = (By.ID, "address2")
        self.country = (By.ID, "country")
        self.state = (By.ID, "state")
        self.city = (By.ID, "city")
        self.zipcode = (By.ID, "zipcode")
        self.mob_number = (By.ID, "mobile_number")

        self.create_account_btn = (By.XPATH, "//button[@data-qa='create-account']")

        self.account_created_msg = (By.CSS_SELECTOR, "h2[data-qa='account-created'] b")
        self.success_msg = (By.CSS_SELECTOR, "#form div[class='row'] p")
        self.continue_btn = (By.CSS_SELECTOR, 'a[data-qa="continue-button"]')

        self.signup_banner = (By.XPATH, "//h2[text()= 'New User Signup!']")
        

    def select_title(self, title):
        self.driver.find_element(self.title[0], self.title[1].format(title)).click()

    def select_date(self, date):
        day, month, year = date.split("-")

        day_dropdown = Select(self.driver.find_element(*self.dob_day))
        month_dropdown = Select(self.driver.find_element(*self.dob_month))
        year_dropdown = Select(self.driver.find_element(*self.dob_year))

        day_dropdown.select_by_value(day)
        month_dropdown.select_by_value(month)
        year_dropdown.select_by_value(year)

    def enter_acc_info(self, info):
        info = json.loads(info)
        self.select_title(info["title"])
        self.driver.find_element(*self.password).send_keys(
            "".join(random.choices(string.ascii_letters + string.digits, k=12))
        )
        self.select_date(info["dob"])

        self.driver.find_element(*self.newsletter_signup).click()
        self.driver.find_element(*self.optin).click()

    def enter_address_info(self, info):
        info = json.loads(info)
        self.driver.find_element(*self.first_name).send_keys(info["first_name"])
        self.driver.find_element(*self.last_name).send_keys(info["last_name"])
        self.driver.find_element(*self.company).send_keys(info["company"])

        self.driver.find_element(*self.address1).send_keys(info["address"]["line1"])
        self.driver.find_element(*self.address2).send_keys(info["address"]["line2"])

        countries = Select(self.driver.find_element(*self.country))
        countries.select_by_value(info["address"]["country"])

        self.driver.find_element(*self.state).send_keys(info["address"]["state"])
        self.driver.find_element(*self.city).send_keys(info["address"]["city"])
        self.driver.find_element(*self.zipcode).send_keys(info["address"]["zipcode"])

        self.driver.find_element(*self.mob_number).send_keys(info["mobile"])

    def hit_create(self):
        self.driver.find_element(*self.create_account_btn).click()

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()
