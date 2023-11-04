# import time
# import undetected_chromedriver as uc
# from undetected_chromedriver import Chrome
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = uc.ChromeOptions()
# opts.add_argument('--disable-extensions')
# opts.add_argument('--disable-logging')
# opts.add_argument('--log-level=3')
# opts.add_argument('--start-maximized')
# opts.add_argument('--disable-notifications')
# opts.add_argument("--disable-gpu")
#
# driver = Chrome(use_subprocess=True, options=opts,headless=True)#, user_data_dir = "c:\temp\profile")#, version_main=117)
# print("Browser Initialized Using Version {driver.capabilities['browserVersion']}")
#
# driver.get("https://nowsecure.nl/")
# time.sleep(30)


import time
import undetected_edgedriver as uc
from undetected_edgedriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = uc.EdgeOptions()
opts.add_argument('--disable-extensions')
opts.add_argument('--disable-logging')
opts.add_argument('--log-level=3')
opts.add_argument('--start-maximized')
opts.add_argument('--disable-notifications')
opts.add_argument("--disable-gpu")

driver = Edge(executable_path=r'D:\driver\msedgedriver.exe',
              use_subprocess=True, options=opts,
              headless=True,
              )  # , user_data_dir = "c:\temp\profile")#, version_main=117)

driver.get("https://nowsecure.nl/")
time.sleep(30)
