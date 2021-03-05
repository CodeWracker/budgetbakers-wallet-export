from selenium import webdriver

def configuration():
    
    driver = webdriver.Firefox(executable_path="..\geckodriver\geckodriver.exe")
    return driver

