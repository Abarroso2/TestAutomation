import platform
from unittest import case
from selenium import webdriver



os_info = platform.system()
driver_path="../driver/"


def before_scenario(context, scenario):
  
  if (os_info == "Linux"):
        pass  
          
     

  if 'web' in context.tags:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    context.browser = webdriver.Chrome(chrome_options=chrome_options,
                              executable_path='../drivers/chromedriver')

    context.browser.implicitly_wait(10)
 
def after_scenario(context, scenario):
  if 'web' in context.tags:
    context.browser.quit()


