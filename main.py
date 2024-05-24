from selenium import webdriver
import time

# Get user input for XPath and Website URL
xpath_value = input("Input the XPath For The Text You Wanna Scrap: ") #/html/body/div[1]/div/h1[2]
website_url = input("Input the Website For The Text You Wanna Scrap: ") #http://automated.pythonanywhere.com

def get_driver(website):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get(website)
    return driver

def clean_text(text):
    """Extract only the temperature from text."""
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver(website_url)
    time.sleep(2)
    element = driver.find_element(by="xpath", value=xpath_value)
    return clean_text(element.text)

print(main())
