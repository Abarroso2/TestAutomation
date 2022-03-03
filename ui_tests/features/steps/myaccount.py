@when(u'i navigate to my account page')
def step_impl(context):
    context.browser.find_element_by_xpath("//header[@id='header']/div[2]/div/div/nav/div/a/span").click()


@then(u'i should see the page with the options to my account')
def step_impl(context):
    pagename=context.browser.find_element_by_xpath("//div[@id='center_column']/h1").text
    assert(pagename=='MY ACCOUNT')
    