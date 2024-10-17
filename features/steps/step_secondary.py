from behave import given, when, then


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.page_secondary.verify_right_page_opens()


@when('Click on Filters')
def click_filters(context):
    context.app.page_secondary.click_filters()


@when('Filter the products by "want to sell"')
def click_filters_sell(context):
    context.app.page_secondary.click_filters_sell()


@when('Click on Apply Filter')
def click_filters_apply(context):
    context.app.page_secondary.click_filters_apply()


@then('Verify all cards have "for sale" page')
def verify_all_cards_have_for_sale(context):
    context.app.page_secondary.verify_all_cards_have_for_sale(context=context)
