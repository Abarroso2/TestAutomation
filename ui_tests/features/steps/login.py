from behave import *
from selenium.webdriver.common.keys import Keys
import unittest

MYSTORE_HOME = 'http://automationpractice.com/index.php'

@given(u'web address "http://automationpractice.com/index.php"')
def step_impl(context):
    context.browser.get(MYSTORE_HOME)

@given(u'login name "allan.barroso@outlook.com" and password newstar1541')
def step_impl(context):
    context.browser.find_element_by_link_text("Sign in").click()
    context.browser.find_element_by_id("email").click()
    context.browser.find_element_by_id("email").clear()
    context.browser.find_element_by_id("email").send_keys("allan.barroso@outlook.com")
    context.browser.find_element_by_id("passwd").click()
    context.browser.find_element_by_id("passwd").clear()
    context.browser.find_element_by_id("passwd").send_keys("newstar1541")
    #context.browser.find_element_by_xpath("//button[@id='SubmitLogin']/span").click()
    
@when(u'i press the sing in button')
def step_impl(context):
    context.browser.find_element_by_xpath("//button[@id='SubmitLogin']/span").click()

@then(u'the site should show my account page and user name')
def step_impl(context):
    name=context.browser.find_element_by_xpath("//header[@id='header']/div[2]/div/div/nav/div/a/span").text
    assert (name == "Allan Barroso")