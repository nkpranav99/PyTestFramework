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
from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions, Edge, EdgeOptions, Ie, IeOptions
from pages.basePage import BasePage
from pages.homePage import HomePage
from pages.login import LoginPage
from pages.signup import SignUpPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Specifies which browser to run the tests on"
    )

@pytest.fixture(scope="function")
def initialize_driver(request):
    driver = request.config.getoption("--browser_name")
    

    match driver.lower():
        case "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            driver = Chrome(options=options)
        case "firefox":
            options = FirefoxOptions()
            options.add_argument("--start_maximized")
            driver = Firefox(options=options)
            driver.maximize_window()
        case "edge":
            options = EdgeOptions()
            options.add_argument("--start_maximized")
            driver = Edge(options=options)
            driver.maximize_window()
        case "ie":
            options = IeOptions()
            options.add_argument("--start_maximized")
            driver = Ie(options=IeOptions)
            driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(initialize_driver):
    return LoginPage(initialize_driver)


@pytest.fixture
def base_page(initialize_driver):
    return BasePage(initialize_driver)


@pytest.fixture
def home_page(initialize_driver):
    return HomePage(initialize_driver)


@pytest.fixture
def sign_up_page(initialize_driver):
    return SignUpPage(initialize_driver)