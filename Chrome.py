from selenium import webdriver
from selenium.webdriver.common.by import By
class Chrome:
    def driver(self):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--incognito")
        chromeOptions.add_argument("--headless")
        return webdriver.Chrome(options=chromeOptions)