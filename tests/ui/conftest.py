import sys
import os

# --- PATH INJECTION FIX START ---
# Get the path to the directory containing conftest.py (tests/ui)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up two levels to the project root (E2E-Automation)
PROJECT_ROOT = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Insert the project root into the Python search path (position 0)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)



import pytest
from selenium.webdriver import Chrome, ChromeOptions
from pages.basePage import BasePage
from pages.homePage import HomePage
from pages.login import LoginPage
from pages.signup import SignUpPage


@pytest.fixture(scope="function")
def initalise_driver():
    options = ChromeOptions()
    options.add_argument("--start-maximized")

    driver = Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(initalise_driver):
    return LoginPage(initalise_driver)


@pytest.fixture
def base_page(initalise_driver):
    return BasePage(initalise_driver)


@pytest.fixture
def home_page(initalise_driver):
    return HomePage(initalise_driver)


@pytest.fixture
def sign_up_page(initalise_driver):
    return SignUpPage(initalise_driver)