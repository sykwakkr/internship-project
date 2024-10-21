from behave import given, when, then


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.page_secondary.verify_right_page_opens()


@when('Click on Filters')
def click_filters(context):
    context.app.page_secondary.click_filters()


@when('Filter the products by "{listing_type}"')
def click_filters_sell(context, listing_type):
    context.app.page_secondary.click_filters_listing_type(listing_type=listing_type)


@when('Click on Apply Filter')
def click_filters_apply(context):
    context.app.page_secondary.click_filters_apply()


@then('Verify all cards have "{sale_tag}')
def verify_all_cards_have_for_sale(context, sale_tag):
    context.app.page_secondary.verify_all_cards_have_correct_tag(context=context, sale_tag=sale_tag)
