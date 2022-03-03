@when(u'i proceed a reorder of an iten')
def step_impl(context):
    context.browser.find_element_by_xpath("//form[@id='submitReorder']/a/span").click()
    context.browser.find_element_by_xpath("//div[@id='center_column']/p[2]/a/span").click()
    context.browser.find_element_by_xpath("//div[@id='center_column']/form/p/button/span").click()
    context.browser.find_element_by_xpath("//form[@id='form']/p/button/span").click()
    context.browser.find_element_by_xpath("//body[@id='order']/div[2]/div/div/a").click()
    context.browser.find_element_by_id("cgv").click()
    context.browser.find_element_by_xpath("//form[@id='form']/p/button/span").click()
    context.browser.find_element_by_link_text("Pay by check (order processing will be longer)").click()
    context.browser.find_element_by_xpath("//p[@id='cart_navigation']/button/span").click()

    confirmation=context.browser.find_element_by_xpath("//div[@id='center_column']/h1").text

    assert(confirmation=='ORDER CONFIRMATION')
    
    context.browser.find_element_by_link_text("Back to orders").click()


@then(u'the order complete page should be displayed')
def step_impl(context):
    pagetitle=context.browser.find_element_by_xpath("//div[@id='center_column']/h1").text
    assert(pagetitle=='ORDER HISTORY')
    