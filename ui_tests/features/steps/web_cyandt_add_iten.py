@when(u'i navigate to dresses section')
def step_impl(context):
    context.browser.find_element_by_xpath("(//a[contains(text(),'Dresses')])[5]").click()


@when(u'i add the Printed Dress to cart')
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@id='center_column']/ul/li/div/div[2]/div[2]/a/span").click()
    context.browser.find_element_by_xpath("//div[@id='layer_cart']/div/div[2]/div[4]/span/span").click()
    context.browser.find_element_by_xpath("(//img[@alt='Printed Dress'])[3]").click()
    context.browser.find_element_by_xpath("//p[@id='add_to_cart']/button/span").click()


@when(u'i verify the cart')
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@id='layer_cart']/div/div[2]/div[4]/span/span").click()


@then(u'the dress should be in the cart')
def step_impl(context):
    context.browser.find_element_by_xpath("//header[@id='header']/div[3]/div/div/div[3]/div/a").click()
    itenbox=context.browser.find_element_by_xpath("(//a[contains(text(),'Printed Dress')])[3]").text
    assert(itenbox=="Printed Dress")