from selenium import webdriver



#def before_all():
      

def before_scenario(context, scenario):


  if 'web' in context.tags:
  #   chrome_options = webdriver.ChromeOptions()
  #   chrome_options.add_argument('--headless')
  #   chrome_options.add_argument('--no-sandbox')
  #   context.browser = webdriver.Chrome(chrome_options=chrome_options,
  #                             executable_path='../drivers/chromedriver')

  #   context.browser.implicitly_wait(10)

      capabilities = {
        "browserName": "chrome",
        "browserVersion": "98.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "startMaximized": True
                        }
                            }

      context.browser = webdriver.Remote(
      command_executor="http://localhost:4444/wd/hub",
      desired_capabilities=capabilities)


 
def after_scenario(context, scenario):
  if 'web' in context.tags:
    context.browser.quit()


