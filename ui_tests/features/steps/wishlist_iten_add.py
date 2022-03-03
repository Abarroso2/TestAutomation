@when(u'i navigate to dress session')
def step_impl(context):
    context.browser.find_element_by_xpath("(//a[contains(text(),'Dresses')])[5]").click()


@when(u'i select a dress and add it to wishlist')
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@id='center_column']/ul/li/div/div[2]/div[2]/a[2]/span").click()
    context.browser.find_element_by_id("wishlist_button").click()
    context.browser.find_element_by_xpath("//body[@id='product']/div[2]/div/div/a").click()

@when(u'i select a second dress and add it to wishlist')
def step_impl(context):
    context.browser.find_element_by_xpath("(//a[contains(text(),'Dresses')])[5]").click()
    context.browser.find_element_by_xpath("//div[@id='center_column']/ul/li[3]/div/div[2]/div[2]/a[2]/span").click()
    context.browser.find_element_by_id("wishlist_button").click()
    context.browser.find_element_by_xpath("//body[@id='product']/div[2]/div/div/a").click()


@when(u'i navigate to the wishlist')
def step_impl(context):
    context.browser.find_element_by_xpath("//header[@id='header']/div[2]/div/div/nav/div/a/span").click()
    context.browser.find_element_by_xpath("//div[@id='center_column']/div/div[2]/ul/li/a/span").click()
    context.browser.find_element_by_link_text("WishlistCI&T").click()


@then(u'the itens should be in the wishlist')
def step_impl(context):
    itens=context.browser.find_element_by_xpath("//tr[@id='wishlist_16322']/td[2]").text
    
    assert(itens!='0')