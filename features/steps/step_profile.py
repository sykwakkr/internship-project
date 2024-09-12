from behave import given, when, then


@when('Enter some test information in the input fields')
def enter_test_info_input_fields(context):
    context.app.page_profile.enter_test_info_input_fields()


@then('Check the right information is present in the input fields')
def check_test_info_input_fields(context):
    context.app.page_profile.check_test_info_input_fields()


@then('Check “Close” and “Save Changes” buttons are available and clickable')
def check_close_save_buttons(context):
    context.app.page_profile.check_close_save_buttons(context.browser_mode)
