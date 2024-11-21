"""
LoginPage.py contains all the methods to the login page

PageObjects file
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Import data
from TestData.data import SauceData
from TestLocators.locators import SauceLocators

class SauceLoginPage:
    # Create the chrome drive object
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Start() Method to launch the URL
    def start(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(SauceData.url)
        return True
    
    # Login() Method
    def login(self):
        self.driver.find_element(by=By.ID, value=SauceLocators.username_locator).send_keys(SauceData.username)
        self.driver.find_element(by=By.ID, value=SauceLocators.password_locator).send_keys(SauceData.password) 
        self.driver.find_element(by=By.ID, value=SauceLocators.login_button_locator).click()
        return True
    # shutdown() method to quit the browser
    def shutdown(self):
        self.driver.quit()
        return None
