import undetected_chromedriver as webdriver
import time

options = webdriver.ChromeOptions()
options.debugger_address = '127.0.0.1:56676'
profile = "C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 21"
options.add_argument(f'user-data-dir={profile}')
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
options.add_argument(f'--disable-gpu')
options.add_argument(f'--no-sandbox')
options.add_argument(f'--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options, use_subprocess=True, headless=True)
driver.get("https://myaccount.google.com/")

time.sleep(1000)
print(driver.title)
