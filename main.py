'''
'''
from selenium import webdriver
import time  
#et option to make browser easy
def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disbale-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disbale-blink-features=AutomationControlled")
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver
\#if we wanna get just the number we can use this
def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output
  
def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

print(main(  ))