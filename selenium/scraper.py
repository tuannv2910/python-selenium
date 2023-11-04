from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options

import time
import random
import os

# ...

user_agent = 'Mozilla/5.0 (Linux; Android 11; 100011886A Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Safari/537.36'
sec_ch_ua = '"Google Chrome";v="104", " Not;A Brand";v="105", "Chromium";v="104"'
referer = 'https://www.google.com'

options = Options()

# set the initial window size
options.add_argument('--window-size=800,600')
driver = webdriver.Chrome(
    options=options,
)
# print the current window size
print(driver.get_window_size())

# change the window size in a
# different way
driver.set_window_size(1920, 1200)

# scraping logic...

# print the new window size
print(driver.get_window_size())  # {"width": 1400, "height": 1200}

driver.get("https://shopee.vn/buyer/login")

timers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

username_xpath = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/input"
password_xpath = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[3]/div[1]/input"
login_xpath = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/button"

# variable
username = "0359233895"
password = "Vantuan2002"


def sleep():
    time.sleep(float(random.choice(timers[0:3]) + random.choice(timers[0:4]) + random.choice(timers[0:9])))


total_unilever_vn_product = 300
total_unilever_vn_beauty_product = 200

wait = WebDriverWait(driver, 20)


def login():
    try:
        driver.get("https://shopee.vn/buyer/login")
        global username_form, password_form, login_button
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, username_xpath)))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, password_xpath)))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, login_xpath)))
    except Exception as ex:
        driver.quit()
        print(ex)
    finally:
        username_form = driver.find_element("xpath", username_xpath)
        password_form = driver.find_element("xpath", password_xpath)
        login_button = driver.find_element("xpath", login_xpath)
        for i in username:
            username_form.send_keys(i)

        for i in password:
            password_form.send_keys(i)

        wait.until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
        login_button.click()

        print(driver.current_url)

        driver.get("https://shopee.vn/unilever_vietnam#product_list")

        for i in range(total_unilever_vn_product):
            response = driver.execute_script(
                "var xhr = new XMLHttpRequest();" + "xhr.open('GET', 'https://shopee.vn/api/v4/shop/rcmd_items?bundle=shop_page_category_tab_main&limit=100&offset=" + str(
                    i) + "&shop_id=111138057&sort_type=1&upstream=', false);" + "xhr.setRequestHeader('Content-Type', 'application/json');" + "xhr.send();" + "return xhr.responseText;")

            print(response)

            # filePath = '../files/' + "unilever_vietnam_offset_" + str(i) + ".json"
            # if not os.path.exists(filePath):
            #     with open(filePath, "w") as file:
            #         pass
            #         file.write(response)
            # else:
            #     with open(filePath, "w") as file:
            #         file.write(response)
            # i += 100

        #
        driver.get("https://shopee.vn/unilevervn_beauty")


login()
