from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


PATH = "/home/uttkarsh/Programming/Python/Selenium/chromedriver"
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
	sleep(0.1)
