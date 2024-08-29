from behave import given, when, then


@given('Open the main page https://soft.reelly.io')
def open_main_page(context):
    context.app.page_main.open_main_page()


@when('Click on settings option')
def click_settings(context):
    context.app.page_main.click_settings()

