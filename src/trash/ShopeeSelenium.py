import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Đường dẫn đến tệp thực thi của trình duyệt (chrome driver)
driver_path = '../driver/msedgedriver.exe'
options = Options()
options.add_argument('--headless=new')
options.binary_location = 'src/driver/msedgedriver.exe'

# Khởi tạo trình duyệt
driver = webdriver.Edge(browser_executable_path='src/driver/msedgedriver.exe', options=options)
# Truy cập trang Shopee
driver.get('https://shopee.vn/buyer/login')

# Đăng nhập
login_button = driver.find_element('navbar__link--account')
login_button.click()

# Tìm và điền thông tin đăng nhập
username_input = driver.find_element_by_id('loginUsername')
username_input.send_keys('TÊN_TÀI_KHOẢN_CỦA_BẠN')

password_input = driver.find_element_by_id('loginPassword')
password_input.send_keys('MẬT_KHẨU_CỦA_BẠN')

# Bấm nút đăng nhập
login_button = driver.find_element_by_class_name('btn--login')
login_button.click()

phoneNumber = "0359233895"
password = "Vantuan2002"

user_name_path = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/input"
password_path = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[3]/div[1]/input"
login_path = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/button"

timers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]


def sleeper():
    time.sleep(float("0." + random.choice(timers[0:3]) + random.choice(timers[0:4]) + random.choice(timers[0:9])))


def login():
    global fieldForm, button_login
    driver.get("https://shopee.vn/buyer/login")

    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, user_name_path)))
        fieldForm = driver.find_element("xpath", user_name_path)
    except Exception as ex:
        print(ex)
        driver.quit()
    finally:
        for i in phoneNumber:
            fieldForm.send_keys(i)
            sleeper()

    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, password_path)))
        fieldForm = driver.find_element("xpath", password_path)
    except Exception as ex:
        print(ex)
        driver.quit()
    finally:
        for i in password:
            fieldForm.send_keys(i)
            sleeper()

    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, login_path)))
        button_login = driver.find_element("xpath", login_path)
    except Exception as ex:
        print(ex)
        driver.quit()
    finally:
        button_login.click()
        sleeper()
    print(driver.title)
    driver.forward()
    print(driver.current_url)


login()
