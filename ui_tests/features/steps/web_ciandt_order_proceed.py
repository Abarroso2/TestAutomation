@when(u'i proceed with the shopping order')
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@id='center_column']/p[2]/a/span").click()
    context.browser.find_element_by_xpath("//div[@id='center_column']/form/p/button/span").click()
    context.browser.find_element_by_xpath("//form[@id='form']/p/button/span").click()
    context.browser.find_element_by_xpath("//body[@id='order']/div[2]/div/div/a").click()
    context.browser.find_element_by_id("cgv").click()
    context.browser.find_element_by_xpath("//form[@id='form']/p/button/span").click()
    context.browser.find_element_by_xpath("//div[@id='HOOK_PAYMENT']/div[2]/div/p/a/span").click()
    context.browser.find_element_by_xpath("//p[@id='cart_navigation']/button/span").click()
    context.browser.find_element_by_xpath("//div[@id='center_column']/p").click()
    context.browser.find_element_by_xpath("//div[@id='center_column']/p").click()
    context.browser.find_element_by_xpath("//div[@id='center_column']/div/h3").click()


@then(u'i should see the order confirmation page')
def step_impl(context):
    confirmation=context.browser.find_element_by_xpath("//div[@id='center_column']/h1").text

    assert(confirmation=='ORDER CONFIRMATION')