#   To run this you should have you browsers drivers installed
#   Link - 
#       For version 84.0.blah-blah = https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/
#       For version 83.0.blah-blah = https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/
#       For version 81.0.blah-blah = please update your chrome(https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.138/)
#   Once installed, replace the value of the variable "PATH"(line no. 17) with the path of the installed driver on your pc
#   For chrome only....

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

PATH = ""
driver = webdriver.Chrome(PATH)

driver.get("https://play.typeracer.com/")

driver.implicitly_wait(10)

try:
    driver.find_element_by_link_text("Cancel").click()      # THIS IS WORKING BUT GIVING AN EXCEPTION GOD HELP ME
except:
    pass                                                    # THAT IS WHY I HAD TO USE "PASS"

driver.find_element_by_link_text("Enter a typing race").click()

driver.implicitly_wait(3)

para = ""
try:
    para += driver.find_element_by_xpath("""//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]""").text
    para += driver.find_element_by_xpath("""//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]""").text + " "
    para += driver.find_element_by_xpath("""//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]""").text
except:
    print("Exception 1 blyat")


enter_the_words = driver.find_element_by_xpath("""//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input""")

try:
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'txtInput')))
except:
    print("HELL NO")

allWords = para.split(" ")

for character in allWords:
	enter_the_words.send_keys(character + " ")
	sleep(0.1)                                      # If you are getting banned increase the sleep value