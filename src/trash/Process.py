import undetected_chromedriver as uc
import selenium as webdriver

# ...
options = uc.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = uc.Chrome(browser_executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",options=options)
driver.get("https://www.tiktok.com/")
# ...


print("title = ", driver.title)



