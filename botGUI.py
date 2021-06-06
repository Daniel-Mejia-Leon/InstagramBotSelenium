from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

root = Tk()
#the screen pops up
root.title('Instagram Bot by Kidd')


def InstaBot(userName, passWord, boxNumber, message):
    picture = "C:\cork360\Documentos\Robot-Video.jpg"
    path = "C:\cork360\Documentos\webDriver\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.instagram.com")
    time.sleep(1)
    # finding the "user here" then placing the user
    bot = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(userName)
    # finding the "pw here" then placing the password
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(passWord)
    # clicking the LOG IN button
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(5)
    # clicking the not now button
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    time.sleep(1)
    # clicking the second not now button
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    time.sleep(1)
    # clicking the inbox
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    time.sleep(2)
    time.sleep(1)
    # clicking the first box
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[' + boxNumber + ']/a').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(
        message)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
    # finding input for the image path
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input').send_keys(picture)
    time.sleep(1)


#just a text
# text = Label(root, text="Instagram Bot", font=("Courier", 44))
# text.pack()
#just a space
space = Label(root, text="")
space.pack()

#just a text
welcomeText = Label(root, text="Welcome to your Instagram bot!", font=("Arial", 20))
welcomeText.pack()
warningText = Label(root, text="Please submit the required information. This bot does not save your information.")
warningText.pack()
sourceText = Label(root, text="You can check the source code at https://github.com/Daniel-Mejia-Leon/InstagramBotSelenium")
sourceText.pack()

#just a space
space = Label(root, text="")
space.pack()

enterUserText = Label(root, text="Place your Instagram user name", font=("Arial", 10))
enterUserText.pack()
#enter your userName
userName = Entry(root, width=50)
userName.pack()
space = Label(root, text="")
space.pack()

enterPasswordText = Label(root, text="Place your Instagram password", font=("Arial", 10))
enterPasswordText.pack()
#enter your password
password = Entry(root, show="*", width=50)
password.pack()
space = Label(root, text="")
space.pack()


number = "1"
message = "this message was sent by a bot"

#code a button to start InstaBot()
startBot = Button(root, text="Start Bot", command=lambda: InstaBot(userName.get(), password.get(), number, message))
startBot.pack()
space = Label(root, text="")
space.pack()
space = Label(root, text="")
space.pack()


# if start:
#     InstaBot(userNameFun(), passwordFun(), number, message)

# text.grid(row=0, column=0)
root.mainloop()
