from behave import *
from selenium import webdriver
from pageObject.login_page import LoginPage


def after_scenario(context, scenario):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()


@given('the user is on the login page')
def step_one(context):
    context.driver = webdriver.Firefox()
    context.login_page = LoginPage(context.driver)
    url = "https://www.saucedemo.com/"
    context.login_page.open(url)


@when('they fill in the credentials correctly')
def step_two(context):
    for row in context.table.rows:
        username = row['user']
        password = row['password']
        context.login_page.enter_credentials(username, password)

        execute_test_for_row(context, username, password)


@then('they should be logged in')
def last_step(context):
    context.login_page.click_button()
    assert context.login_page.home_page_is_displayed()
    context.driver.quit()


def execute_test_for_row(context, username, password):
    context.login_page.open("https://www.saucedemo.com/")
    context.login_page.enter_credentials(username, password)


@when('they fill in the credentials correctly however is blocked')
def step_three(context):
    for row in context.table.rows:
        username = row['user']
        password = row['password']
        context.login_page.enter_credentials(username, password)

        execute_test_for_row(context, username, password)
    context.login_page.click_button()


@then('should displayed error message')
def step_four(context):
    context.login_page.error_message_is_displayed()
    context.driver.quit()


@when('change the order of credentials')
def step_five(context):
    for row in context.table.rows:
        password = row['user']
        username = row['password']


@Then('should be view error message')
def step_six(context):
    context.login_page.click_button()
    context.login_page.error_message_is_displayed()
    context.driver.quit()
