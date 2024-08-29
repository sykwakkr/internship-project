from behave import given, when, then


@when('Click on Edit profile option')
def click_edit_profile(context):
    context.app.page_settings.click_edit_profile()
