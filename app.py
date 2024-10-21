from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

PRN = '{YOUR_PRN}'
PHONE = '{YOUR_PHONE}'

url = 'http://192.168.1.8:8090/httpclient.html'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  
chrome_options.add_argument("--log-level=3")  
chrome_options.add_argument("--silent")  


chrome_driver_path = './chromedriver.exe'
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

try:
    
    driver.get(url)
    time.sleep(2)
    
    username_field = driver.find_element(By.ID, 'username')
    username_field.clear()
    username_field.send_keys(PRN)
    
    password_field = driver.find_element(By.ID, 'password')
    password_field.clear()
    password_field.send_keys(PHONE)
    
    login_button = driver.find_element(By.ID, 'loginbutton')
    login_button.click()
    
    time.sleep(5)
    
    print("Login successful. The browser will remain open even though the script has terminated.")

finally:
    print("Script finished execution.")
