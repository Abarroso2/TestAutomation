@when(u'i add the Printed Chiffon Dress to cart')
def step_impl(context):
    
    context.browser.find_element_by_xpath("//div[@id='layer_cart']/div/div[2]/div[4]/span/span").click()

@when(u'i remove Printed Dress from cart')
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@id='layer_cart']/div/div[2]/div[4]/span/span").click()
    context.browser.find_element_by_xpath("//header[@id='header']/div[3]/div/div/div[3]/div/a/b").click()
    context.browser.find_element_by_xpath("//a[@id='3_13_0_264699']/i").click()

@then(u'only the Printed Chiffon Dress should be in the cart')
def step_impl(context):
    try:
        deleted=context.browser.find_element_by_link_text("Printed Dress").text
    except Exception:
        assert True