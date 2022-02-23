import time
import keyboard

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# disable bot detection on chrome/BestBuy
options = Options()

# for using the browser
browser = webdriver.Chrome('C:\webdrivers\chromedriver.exe',options=options)

# cookie clicker site url
cookie_site = "https://orteil.dashnet.org/cookieclicker/"
time.sleep(1)

browser.get(cookie_site)

# wait for cookie button to load
WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.ID, 'bigCookie')))  

loop2 = True
loop1 = True
while loop1:

    # press 'a' to unpause the auto-clicker
    if keyboard.is_pressed('a'): 
            print('a pressed')
            loop2 = True
            time.sleep(0.5)

    while loop2:
        cookieBtn = addButton = browser.find_element_by_id('bigCookie')
        
        cookieBtn.click()
        
        # press 'a' to unpause the auto-clicker
        if keyboard.is_pressed('a'): 
            print('a pressed')
            loop2 = False
            time.sleep(0.5)
