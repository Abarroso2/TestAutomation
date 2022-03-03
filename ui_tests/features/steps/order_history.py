@when(u'i navigate to my order history')
def step_impl(context):
    context.browser.find_element_by_xpath("//header[@id='header']/div[2]/div/div/nav/div/a/span").click()
    context.browser.find_element_by_xpath("//div[@id='center_column']/div/div/ul/li/a/span").click()


@then(u'i should be able to see my order history page')
def step_impl(context):
    pagename=context.browser.find_element_by_xpath("//div[@id='center_column']/h1").text
    assert(pagename=="ORDER HISTORY")