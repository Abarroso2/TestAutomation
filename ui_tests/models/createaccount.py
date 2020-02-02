from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CreateAccount():
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def navigate(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        driver.find_element_by_link_text("Sign in").click()
    
    def mailcreate():
        driver.find_element_by_id("email_create").click()
        driver.find_element_by_id("email_create").clear()
        driver.find_element_by_id("email_create").send_keys("allan.barroso@outlook.com")
        driver.find_element_by_id("create-account_form").submit()

    def genderselect(self, recgender):
        if (recgender == masculino)    
            driver.find_element_by_id("id_gender1").click()
        else
            driver.find_element_by_id("id_gender2").click()

        driver.find_element_by_xpath("//form[@id='account-creation_form']/div/div[2]").click()
        
        
    def namefield(self):
        driver.find_element_by_id("customer_firstname").click()
        driver.find_element_by_id("customer_firstname").clear()
        driver.find_element_by_id("customer_firstname").send_keys("Allan")
        driver.find_element_by_id("customer_lastname").clear()
        driver.find_element_by_id("customer_lastname").send_keys("Barroso")
    
    def passwordselect():
        driver.find_element_by_id("passwd").clear()
        driver.find_element_by_id("passwd").send_keys("newstar1541")
        
    def ageselect(self):
        driver.find_element_by_id("days").click()
        Select(driver.find_element_by_id("days")).select_by_visible_text("regexp:22\\s+")
        driver.find_element_by_xpath("//option[@value='22']").click()
        driver.find_element_by_id("months").click()
        Select(driver.find_element_by_id("months")).select_by_visible_text("regexp:September\\s")
        driver.find_element_by_xpath("(//option[@value='9'])[2]").click()
        driver.find_element_by_id("years").click()
        Select(driver.find_element_by_id("years")).select_by_visible_text("regexp:1981\\s+")
        driver.find_element_by_xpath("//option[@value='1981']").click()

    def companyname(self):    
        driver.find_element_by_id("company").click()
        driver.find_element_by_id("company").clear()
        driver.find_element_by_id("company").send_keys("home test")
        
    def address    
        driver.find_element_by_id("address1").click()
        driver.find_element_by_id("address1").clear()
        driver.find_element_by_id("address1").send_keys("street spirit 666")
        driver.find_element_by_id("city").click()
        driver.find_element_by_id("city").clear()
        driver.find_element_by_id("city").send_keys("Las Vegas")
        driver.find_element_by_id("id_state").click()
        driver.find_element_by_id("id_state").click()
        driver.find_element_by_id("id_state").click()
        Select(driver.find_element_by_id("id_state")).select_by_visible_text("Texas")
        driver.find_element_by_xpath("//option[@value='43']").click() 
        driver.find_element_by_id("postcode").click()
        driver.find_element_by_id("postcode").clear()
        driver.find_element_by_id("postcode").send_keys("89109")
        driver.find_element_by_id("other").click()
        driver.find_element_by_id("other").clear()
        driver.find_element_by_id("other").send_keys("teste")

def contact(self)
        driver.find_element_by_id("phone").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("+5531994769506")
        driver.find_element_by_id("alias").click()
        driver.find_element_by_id("phone_mobile").click()
        driver.find_element_by_id("phone_mobile").clear()
        driver.find_element_by_id("phone_mobile").send_keys("+5531994769506")
        driver.find_element_by_id("account-creation_form").click()
        driver.find_element_by_id("alias").click()
        driver.find_element_by_xpath("//form[@id='account-creation_form']/div/div[5]").click()
        driver.find_element_by_id("optin").click()
        driver.find_element_by_id("optin").click()
        driver.find_element_by_id("newsletter").click()
        driver.find_element_by_id("optin").click()

def submission(self):
        driver.find_element_by_xpath("//button[@id='submitAccount']/span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()