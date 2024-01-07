from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

for i in range(5) :   
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options) 
    
    url1 = "https://daum.net/" # 1 STEP : 다음 접속
    driver.get(url1)
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    time.sleep(1)