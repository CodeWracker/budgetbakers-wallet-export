from selenium import webdriver
import os

FILE_PATH = os.getcwd() + "//../site/"
# PUT THE HTML FILE NAME HERE, I USE "REGISTROS-WALLET-P" BY DEFAULT
FILE_PATH = FILE_PATH + "registros-wallet-p.html"

def configuration():
    
    driver = webdriver.Firefox(executable_path=".\geckodriver\geckodriver.exe")
    return driver

