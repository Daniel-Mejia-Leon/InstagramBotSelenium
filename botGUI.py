from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import cv2
import time

root = Tk()
root.title('Instagram Bot by Kidd')

start = False


# root.geometry("400x600")
def userNameFun():
    displayUserName = Label(root, text=userName.get())
    displayUserName.pack()
    return userName.get()


class passBool:
    start = False

    def passwordFun(self):
        displayPassword = Label(root, text=password.get())
        displayPassword.pack()
        return password.get()

    def starter(self):
        self.start = True


text = Label(root, text="Instagram Bot")
text.pack()

space = Label(root, text="")
space.pack()

welcomeText = Label(root,
                    text="Welcome to Instagram bot by Kidd. Please submit the required information. This bot does not save your information, you can check the source code at https://github.com/Daniel-Mejia-Leon/InstagramBotSelenium")
welcomeText.pack()

userName = Entry(root, width=50)
userName.pack()
button = Button(root, text="Submit", command=userNameFun)
button.pack()

password = Entry(root, width=50)
password.pack()
button = Button(root, text="Submit", command=passBool.passwordFun)
button.pack()

number = "2"
message = "BotGui"


def InstaBot(userName, passWord, boxNumber, message):
    picture = "C:\cork360\Documentos\Robot-Video.jpg"
    image = cv2.imread("C:\cork360\Documentos\Robot-Video.jpg")
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
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input').send_keys(image)
    time.sleep(1)


if passBool.starter:
    InstaBot(userNameFun(), passBool.passwordFun, number, message)

# text.grid(row=0, column=0)
root.mainloop()
