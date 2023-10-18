from behave import *



def execute_test_for_password(context, password):
    context.login_page.open("https://www.saucedemo.com/")
    context.login_page.enter_password(password)


@when("fill password's field")
def step_two(context):
    for row in context.table.rows:
        password = row['password']
        context.login_page.enter_password(password)
        context.password = password

        execute_test_for_password(context, password)
    context.login_page.click_button()


@Then ('each input should displayed *')
def step_three(context):
    password = context.login_page.password_asterisks()
    if password != "*" * len(context.password):
        assert isinstance(password, object)
        print(password)
    assert password == "*" * len(password)

    context.browser.quit()

    
