import random
import string
from pages.signup import SignUpPage
from pages.basePage import BasePage


def test_valid_user_registration(
    initalise_driver, base_page, home_page, sign_up_page, login_page
):
    base_page.open("https://automationexercise.com/")
    base_page.wait_until_element_visible(home_page.logo)

    base_page.click_on_element(home_page.signup)
    base_page.wait_until_element_visible(sign_up_page.signup_banner)

    login_page.register(
        f"test{"".join(random.choices(string.ascii_letters + string.digits, k=3))}",
        f"test{"".join(random.choices(string.ascii_letters + string.digits, k=3))}@test.com",
    )
    base_page.wait_until_element_visible(sign_up_page.acc_info_heading)

    # sign_up_page.select_title("Mr")
    sign_up_page.enter_acc_info('{"title":"Mr", "dob":"3-8-1999"}')
    base_page.click_on_element(sign_up_page.newsletter_signup)
    base_page.click_on_element(sign_up_page.optin)

    sign_up_page.enter_address_info('{"first_name": "Test", "last_name": "Test", "company": "Test pvt. ltd", "address": {"line1": "Test1","line2": "test2","country": "Singapore","state": "test","city": "test","zipcode": "230912"},"mobile": "9999991233"}')
    base_page.click_on_element(sign_up_page.create_account_btn)

    base_page.wait_until_element_visible(sign_up_page.success_msg)
    base_page.click_on_element(sign_up_page.continue_btn)


