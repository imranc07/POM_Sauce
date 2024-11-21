"""
test_login.py contains the test cases


Test Scripts File
"""
from PageObjects.LoginPage import SauceLoginPage


# test case for starting automation
def test_start():
    assert SauceLoginPage().start() == True
    print("SUCCESS : Automation started!")


# test case for login Sauce Demo
def test_login():
    assert SauceLoginPage().login() == True
    print("SUCCESS : Logged In!")


# test case for shutdown the browser
def test_shutdown():
    assert SauceLoginPage().shutdown() == None  
    print("SUCCESS : Automation shutdown!")
