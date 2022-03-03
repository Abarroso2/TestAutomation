@when(u'i navigate to wishlist')
def step_impl(context):
    context.browser.find_element_by_xpath("//header[@id='header']/div[2]/div/div/nav/div/a/span").click()
    context.browser.find_element_by_xpath("//div[@id='center_column']/div/div[2]/ul/li/a/span").click()


@when(u'i create a new wishlist')
def step_impl(context):
    context.browser.find_element_by_id("name").click()
    context.browser.find_element_by_id("name").clear()
    context.browser.find_element_by_id("name").send_keys("WishlistCI&T")
    context.browser.find_element_by_xpath("//button[@id='submitWishlist']/span").click()


@then(u'the wishlist should be created')
def step_impl(context):
    wishlistname=context.browser.find_element_by_xpath("//a[contains(text(),'WishlistCI&T')]").text
    assert(wishlistname=="WishlistCI&T") 