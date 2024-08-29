from behave import given, when, then


@when('Log in to the page')
def log_in_to_the_page(context):
    context.app.page_signin.log_in_to_the_page()