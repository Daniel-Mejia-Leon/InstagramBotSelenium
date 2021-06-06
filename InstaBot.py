from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import cv2
import time
from secretStuff import secretInsta

picture = "C:\cork360\Documentos\Robot-Video.jpg"
image = cv2.imread("C:\cork360\Documentos\Robot-Video.jpg")

path = "C:\cork360\Documentos\webDriver\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com")
time.sleep(1)
#finding the "user here" then placing the user
bot = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('Insta_melach')
#finding the "pw here" then placing the password
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(secretInsta())
#clicking the LOG IN button
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(5)
#clicking the not now button
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(1)
#clicking the second not now button
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
time.sleep(1)
#clicking the inbox
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
time.sleep(2)
#clicking the first box
driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a').click()
time.sleep(1)
#clicking the textInput
#driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys("test")

#finding input for the image path
sendingPic = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input').send_keys(picture)


def selectClickAndSend(box, message):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[' + box + ']/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')\
        .send_keys(message)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
