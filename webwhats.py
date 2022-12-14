from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


WP_LINK = 'https://web.whatsapp.com'
NEW_CHAT = '//*[@id="side"]/header/div[2]/div/spam/div[2]/div'
WP_LINK = 'https://web.whatsapp.com'

driver = webdriver.Chrome()             #tem que ter o executável chromedriver_win32.exe na mesma pasta
driver.get(WP_LINK)

# while True:
#     sleep(20)
#     break

contador = True
while contador:
    sleep(3)
    try:
        driver.find_element(By.XPATH, NEW_CHAT)
        contador = False
    except:
        print('Por favor scaneie o QR Code')
        contador = True





