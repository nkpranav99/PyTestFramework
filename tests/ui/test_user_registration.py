import json
import random
import string

import pytest

test_data_path = "test_data/test.json"

with open(test_data_path) as f:
    test_data = json.load(f)
    test_inputs = test_data["data"]


@pytest.mark.parametrize("test_input", test_inputs)
@pytest.mark.smoke
def test_valid_user_registration_and_deletion(
    initialize_driver, base_page, home_page, sign_up_page, login_page, test_input
):
    base_page.open(test_input["baseUrl"])
    base_page.wait_until_element_visible(home_page.logo)

    base_page.click_on_element(home_page.signup)
    base_page.wait_until_element_visible(sign_up_page.signup_banner)

    login_page.register(
        f"test{"".join(random.choices(string.ascii_letters + string.digits, k=3))}",
        f"test{"".join(random.choices(string.ascii_letters + string.digits, k=3))}@test.com",
    )
    base_page.wait_until_element_visible(sign_up_page.acc_info_heading)

    # sign_up_page.select_title("Mr")
    sign_up_page.enter_acc_info(
        f'{{"title":"{test_input["user_info"]["title"]}", "dob":"{test_input["user_info"]["dob"]}"}}'
    )
    base_page.click_on_element(sign_up_page.newsletter_signup)
    base_page.click_on_element(sign_up_page.optin)

    sign_up_page.enter_address_info(
    f'{{'
    f'"first_name": "{test_input["user_info"]["address_info"]["first_name"]}", '
    f'"last_name": "{test_input["user_info"]["address_info"]["last_name"]}", '
    f'"company": "{test_input["user_info"]["address_info"]["company"]}", '
    f'"address": {{'
        f'"line1": "{test_input["user_info"]["address_info"]["address"]["line1"]}", '
        f'"line2": "{test_input["user_info"]["address_info"]["address"]["line2"]}", '
        f'"country": "{test_input["user_info"]["address_info"]["address"]["country"]}", '
        f'"state": "{test_input["user_info"]["address_info"]["address"]["state"]}", '
        f'"city": "{test_input["user_info"]["address_info"]["address"]["city"]}", '
        f'"zipcode": "{test_input["user_info"]["address_info"]["address"]["zipcode"]}"'
    f'}}, '
    f'"mobile": "{test_input["user_info"]["address_info"]["mobile"]}"'
    f'}}'
)
    base_page.click_on_element(sign_up_page.create_account_btn)

    base_page.wait_until_element_visible(sign_up_page.success_msg)
    base_page.click_on_element(sign_up_page.continue_btn)

    base_page.wait_until_element_visible(home_page.logo)

    home_page.verify_logged_in_user()
    home_page.delete_user()
    home_page.verify_user_deletion()
