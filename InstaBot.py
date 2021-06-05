from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from secretStuff import secretInsta

path = "C:\cork360\Documentos\webDriver\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com")
time.sleep(1)
bot = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('Insta_melach')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(secretInsta())
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
time.sleep(2)

def selectClickAndSend(box, message):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[' + box + ']/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')\
        .send_keys(message)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

boxNumber1 = "1"
boxNumber2 = "2"
boxNumber3 = "3"
boxNumber4 = "4"
messageToSend = "test"

selectClickAndSend(boxNumber1, messageToSend)
selectClickAndSend(boxNumber2, messageToSend)
selectClickAndSend(boxNumber3, messageToSend)
selectClickAndSend(boxNumber4, messageToSend)