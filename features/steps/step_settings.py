from behave import given, when, then


@when('Click on Edit profile option')
def click_edit_profile(context):
    context.app.page_settings.click_edit_profile()


@then('Verify the right {url_page} page opens')
def verify_right_page_open(context, url_page):
    context.app.page_settings.verify_settings_page_open(url_page)


@then('Verify there are {12} options for the settings')
def verify_settings_page_options(context, number_of_options):
    context.app.page_settings.verify_settings_options(number_of_options)


@then('Verify "{option}" button is available')
def verify_option_button(context, option):
    context.app.page_settings.verify_option_button(option, context.browser_mode)

