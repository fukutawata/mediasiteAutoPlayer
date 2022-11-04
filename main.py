import sys

args = sys.argv

print(args[0])
print(args[1])
referencePath = str(args[1])
sys.path.append(referencePath)
import chromedriver_binary
import datetime
import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


#the difinition of id and password
guestUsername = None
guestPassword = None
startTest = True

# print(__file__)
filepath = str(__file__)
filepath = filepath.replace("/main.py","")
# print(filepath)
#open txt file
f = open(filepath+'/guestInformation.txt', 'r')
datalist = f.readlines()
guestmainUsername = datalist[0]
guestmainPassword = datalist[1]
f.close()

#if username is not resistered ;input
if (guestmainUsername=="UserID\n"):
    guestUsername = input("UserID:")
    guestPassword = input("Password:")
    f = open(filepath+'/guestInformation.txt', 'w')
    f.write(guestUsername)
    f.write("\n")
    f.write(guestPassword)
    f.close()
    guestmainUsername = guestUsername
    guestmainPassword = guestPassword

#confirmation of manaba-program operation
driver = webdriver.Chrome()
driver.get('https://www.ecloud.tsukuba.ac.jp/manaba')
driver.find_element(By.PARTIAL_LINK_TEXT,value='manabaのログインページへ').click()
driver.find_element(By.ID,value="username").send_keys(guestmainUsername)
driver.find_element(By.ID,value="password").send_keys(guestmainPassword)
driver.find_element(By.NAME,value='_eventId_proceed').click()
startTest =False
time.sleep(2)
driver.close()

global jobtest
jobtest = True

#the definiton of job()
def job(URL,duration):
    #global driver
    driver = webdriver.Chrome()
    driver.get('https://www.ecloud.tsukuba.ac.jp/manaba')
    driver.find_element(By.PARTIAL_LINK_TEXT,value='manabaのログインページへ').click()
    driver.find_element(By.ID,value="username").send_keys(guestmainUsername)
    driver.find_element(By.ID,value="password").send_keys(guestmainPassword)
    driver.find_element(By.NAME,value='_eventId_proceed').click()
    driver.get(URL)
    time.sleep(2)
    ActionChains(driver).move_to_element_with_offset(driver.find_element(By.TAG_NAME,'body'), 200, 200).click().perform()
    global jobtest 
    jobtest = False
    time.sleep(duration)
    driver.close()
    #driver.find_element(By.CLASS_NAME,value='play-button').click()


def work_1(start_time,duration,lesson_url):
    global jobtest 
    jobtest = True

    schedule.every().monday.at(start_time).do(job,lesson_url,duration)

    while jobtest:
        schedule.run_pending()
        time.sleep(1)

def work_2(start_time,duration,lesson_url):
    global jobtest 
    jobtest = True

    schedule.every().tuesday.at(start_time).do(job,lesson_url,duration)
     

    while jobtest:
        schedule.run_pending()
        time.sleep(1)

def work_3(start_time,duration,lesson_url):
    global jobtest 
    jobtest = True

    schedule.every().wednesday.at(start_time).do(job,lesson_url,duration)

    while jobtest:
        schedule.run_pending()
        time.sleep(1)

def work_4(start_time,duration,lesson_url):
    global jobtest 
    jobtest = True

    schedule.every().thursday.at(start_time).do(job,lesson_url,duration)

    while jobtest:
        schedule.run_pending()
        time.sleep(1)

def work_5(start_time,duration,lesson_url):
    global jobtest 
    jobtest = True

    schedule.every().friday.at(start_time).do(job,lesson_url,duration)

    while jobtest:
        schedule.run_pending()
        time.sleep(1)
#####



 
# current time
now = datetime.datetime.now()

#execute sample
if (now < datetime.datetime(2022,11,8,10, 8, 0)):
    work_2("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_2("12:13",10500,"https://xxxxxxxxxxxxxxxx")
    work_2("15:13",5100,"https://xxxxxxxxxxxxxxxx")
    work_3("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_3("12:13",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("12:13",5100,"https://xxxxxxxxxxxxxxxx")

if (now > datetime.datetime(2022,11,8,10, 8, 1) and now < datetime.datetime(2022,11,8,12, 13, 0)):
    work_2("12:13",10500,"https://xxxxxxxxxxxxxxxx")
    work_2("15:13",5100,"https://xxxxxxxxxxxxxxxx")
    work_3("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_3("12:13",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("12:13",5100,"https://xxxxxxxxxxxxxxxx")

if (now > datetime.datetime(2022,11,8,12, 13, 1) and now < datetime.datetime(2022,11,8,15, 13, 0)):
    work_2("15:13",5100,"https://xxxxxxxxxxxxxxxx")
    work_3("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_3("12:13",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("12:13",5100,"https://xxxxxxxxxxxxxxxx")

if (now > datetime.datetime(2022,11,8,15, 13, 1) and now < datetime.datetime(2022,11,9,10, 8, 0)):
    work_3("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_3("12:13",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("12:13",5100,"https://xxxxxxxxxxxxxxxx")

if (now > datetime.datetime(2022,11,9,10, 8, 1) and now < datetime.datetime(2022,11,9,12, 13, 0)):
    work_3("12:13",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("12:13",5100,"https://xxxxxxxxxxxxxxxx")


if (now > datetime.datetime(2022,11,9,12, 13, 1) and now < datetime.datetime(2022,11,11,10, 8, 0)):
    work_5("10:08",5100,"https://xxxxxxxxxxxxxxxx")
    work_5("12:13",5100,"https://xxxxxxxxxxxxxxxx")

if (now > datetime.datetime(2022,11,11,10, 8, 1) and now < datetime.datetime(2022,11,11,12, 13, 0)):
    work_5("12:13",5100,"https://xxxxxxxxxxxxxxxx")

if (now > datetime.datetime(2022,11,11,12, 13, 1)):
    print("The program is not usable. Prease get the latest version.")

