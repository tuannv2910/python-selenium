import undetected_edgedriver as webdriver

options = webdriver.EdgeOptions()
options.debugger_address = '127.0.0.1:56676'
profile = "	C:\\Users\\Admin\\AppData\\Local\\Microsoft\\Edge\\User Data\\Profile 1"
options.add_argument(f'user-data-dir={profile}')
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
options.add_argument(f'--disable-gpu')
options.add_argument(f'--no-sandbox')
options.add_argument(f'--disable-dev-shm-usage')
options.executable_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Set the executable path using the Service class
# service = Service(r'C:\Users\Admin\Desktop\python\pythonProject\src\driver\msedgedriver.exe')

# Create a new Edge driver
driver = webdriver.Edge(
    # service=service, options=options,
    use_subprocess=True, headless=True)

# Get the page title
driver.get("https://myaccount.google.com/")
print(driver.title)
