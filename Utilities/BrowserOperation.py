from configparser import ConfigParser

from selenium import webdriver

from ObjectRepository.Login import ElementLogin
from Utilities import Utility

configDriver=ConfigParser()
configDriver.read(Utility.projectDirectory()+"\\Configuration\\config.ini")

def launchBrowser():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path= Utility.projectDirectory()+"\\chromedriver.exe",options=chrome_options)
    Utility.maximize(driver)
    Utility.implicitWait(driver, 10)
    return driver


def login():
    pass


def launchFlipkart():
    driver = launchBrowser()
    Utility.get(driver, configDriver.get("Credential", "link"))
    login()
    return driver


def refreshLogin(driver):
    login()


launchFlipkart()