@when(u'i select an iten in the list and click on it datails')
def step_impl(context):
    context.browser.find_element_by_xpath("//table[@id='order-list']/tbody/tr/td/span").click()
    context.browser.find_element_by_xpath("//table[@id='order-list']/tbody/tr[2]/td/div/div[3]/div[2]/a/span/i").click()


@then(u'i should be able to see the details about the item selected')
def step_impl(context):
    detailsdelivery=context.browser.find_element_by_xpath("//div[@id='block-order-detail']/div[4]/div/div/ul/li/h3").text
    assert(detailsdelivery=='DELIVERY ADDRESS (MY ADDRESS)')