from json import load
from os import path, pardir
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def before_all(context):
    if context.config.userdata.get("browser") == None:
        context.config.userdata["browser"] = "chrome"

    if context.config.userdata["browser"].lower() == "firefox":
        options = FirefoxOptions()
        options.set_capability("browserVersion", "latest")
        options.set_capability("platformName", "any")
        options.browser_version = "stable"
        options.timeouts = {"script": 5000, "pageLoad": 5000}
        if context.config.userdata.get("headless"):
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
        if context.config.userdata.get("headless"):
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
