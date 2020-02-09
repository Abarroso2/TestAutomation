from selenium import webdriver
 
def before_scenario(context, scenario):
  if 'web' in context.tags:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    context.browser = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path='/home/abarroso/CIandTgithub/CIandT/ui_tests/drivers/chromedriver')
    #context.browser = webdriver.Crome(executable_path='/home/abarroso/CIandTgithub/CIandT/uitests-old/drivers/chromedriver')
    context.browser.implicitly_wait(10)
 
def after_scenario(context, scenario):
  if 'web' in context.tags:
    context.browser.quit()



