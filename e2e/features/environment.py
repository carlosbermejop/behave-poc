from json import load
from os import path, pardir
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from behave.log_capture import capture
import logging

PRE_FLIGHT_CHECK = None


def before_all(context):
    context.config.setup_logging()
    is_api_test = any(tag in context.config.tags for tag in ["@api", "@local"])
    if context.config.userdata.get("browser") == None:
        context.config.userdata["browser"] = "chrome"

    if context.config.userdata["browser"].lower() == "firefox":
        options = FirefoxOptions()
        options.set_capability("browserVersion", "latest")
        options.set_capability("platformName", "any")
        options.browser_version = "stable"
        options.timeouts = {"script": 5000, "pageLoad": 5000}
        if context.config.userdata.get("headless") or is_api_test:
            options.add_argument("-headless")
            options.add_argument("--width=1325")
            options.add_argument("--height=744")
        context.browser = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        options.set_capability("browserVersion", "latest")
        options.set_capability("platformName", "any")
        options.browser_version = "stable"
        options.timeouts = {"script": 5000, "pageLoad": 5000}
        if context.config.userdata.get("headless") or is_api_test:
            options.add_argument("--window-size=1400,800")
            options.add_argument("--headless=new")
        context.browser = webdriver.Chrome(options=options)

    context.browser.implicitly_wait(5)
    if context.config.userdata.get("headless") == None:
        context.browser.maximize_window()

    profile = context.config.userdata.get("profile", "dev")
    config_file = path.abspath(
        path.join(path.dirname(__file__), pardir, "config", f"{profile}.json")
    )
    if path.exists(config_file):
        with open(config_file) as f:
            profile_config = load(f)
        context.config.update_userdata(profile_config)


@capture
def before_scenario(context, scenario):
    tags_to_skip = ["skip", "wip", "no", "draft"]
    global PRE_FLIGHT_CHECK
    is_tag_to_skip = any(tag_to_check in scenario.tags for tag_to_check in tags_to_skip)
    if is_tag_to_skip:
        scenario.skip()

    is_api_test = any(
        tag_to_check in scenario.tags for tag_to_check in ["api", "local"]
    )

    if is_api_test:
        try:
            PRE_FLIGHT_CHECK = requests.get("http://localhost:5000/api/health")
        except requests.exceptions.ConnectionError:
            pass
        finally:
            if PRE_FLIGHT_CHECK.status_code != 200:
                scenario.skip(
                    "The scenario was skipped because the API could not be reached."
                )
            PRE_FLIGHT_CHECK = None
