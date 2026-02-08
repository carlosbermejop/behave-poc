from behave import (
    Given as Given,
    Step as Step,
    Then as Then,
    When as When,
    fixture as fixture,
    given as given,
    register_type as register_type,
    step as step,
    step_matcher as step_matcher,
    then as then,
    use_default_step_matcher as use_default_step_matcher,
    use_fixture as use_fixture,
    use_step_matcher as use_step_matcher,
    when as when,
)
from selenium.webdriver.common.by import By


@given("The user navigates to the Behave documentation website")
def step_impl(context):
    context.browser.get(context.config.userdata.get("online_base_url"))
    assert context.browser.title == "behave 1.4.0.dev0 documentation"


@then("They land on the welcome section")
def step_impl(context):
    context.browser.find_element(By.ID, "welcome-to-behave").is_displayed()


@when("They navigate to the {section_name} menu")
def step_impl(context, section_name):
    burger_menu_btn = context.browser.find_element(By.CLASS_NAME, "nav-overlay-icon")
    if burger_menu_btn.is_displayed():
        burger_menu_btn.click()
    menu_item = context.browser.find_element(By.LINK_TEXT, section_name)
    menu_item.click()


@then("They are redirected to the correct page for {section_id} menu")
def step_impl(context, section_id):
    assert context.browser.find_element(By.ID, section_id).is_displayed()
