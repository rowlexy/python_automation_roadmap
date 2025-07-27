# Scraping data from the website and saving the values into a text file

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt
import time, sys

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get('http://automated.pythonanywhere.com/login/')
    return driver

def extract_number(text):
    output = text.split(': ')[-1]
    return output

def save_file(text):
    file_name = dt.now().strftime('%Y-%m-%d.%H:%M:%S')
    with open(f'{file_name}.txt', 'w') as file:
        file.write(text)
    

def main():
    driver = get_driver()
    driver.find_element(by='id', value='id_username').send_keys('automated')
    driver.find_element(by='id', value='id_password').send_keys('automatedautomated' + Keys.RETURN)
    time.sleep(5)
    try:
        while True:
            driver.find_element('xpath', '/html/body/nav/div/a').click()
            time.sleep(5)
            text_extract = driver.find_element('xpath', '/html/body/div[1]/div/h1[2]').text
            time.sleep(5)
            number = extract_number(text_extract)
            save_file(number)
    except KeyboardInterrupt:
        sys.exit()
    
    
main()