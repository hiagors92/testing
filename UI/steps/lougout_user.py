from behave import *
from pageObject.login_page import LoginPage
from selenium import webdriver


@given ('the user logged')
def step_user_logged(context):
    context.driver = webdriver.Firefox()
    context.login_page = LoginPage(context.driver)
    url = "https://www.saucedemo.com/"
    context.login_page.open(url)
    context.login_page.enter_credentials(username="standard_user", password="secret_sauce")
    context.login_page.click_button()
    context.login_page.home_page_is_displayed()

@when ('click to logout')
def step_two(context):
    context.login_page.menu()

@then ('Should be redirection to login page')
def step_three(context):
    LoginPage.logout(context)
    context.driver.quit()