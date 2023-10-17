from behave import *
from selenium import webdriver
from pageObject.login_page import LoginPage


def after_scenario(context, scenario):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()

@when('not field username and password')
def step_input_empty(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.input_empty()


@then('login button should be disabled')
def step_button_disabled(context):
    context.login_page.click_button()
    context.login_page.error_message_is_displayed()
    context.driver.quit()
