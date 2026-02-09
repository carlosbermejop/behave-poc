from behave import (
  then,
  when
)
import requests
from selenium.webdriver.common.by import By

@when("The user calls /user/ with an username")
def step_impl(context):
  response = requests.get("http://localhost:5000/user/Test")
  assert response.status_code == 200
  context.api_response = response
  
@then("The response includes the username correctly")
def step_impl(context):
  assert context.api_response.text == "User Test"
  
@then("This test should always be skipped")
def step_impl(context):
  # The body of this test is empty to showcase the @skip functionality
  pass