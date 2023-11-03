from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import undetected_edgedriver as uc


def crawl_data_edge():
    options = uc.EdgeOptions()
    # options.add_argument('--headless')
    options.add_argument("--window-size=800,600")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    user_profile_path = r'C:\Users\Admin\AppData\Local\Microsoft\Edge\User Data'
    options.add_argument(f'user-data-dir={user_profile_path}')
    options.add_argument(f'profile-directory=Profile 1')
    options.executable_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    driver = uc.Edge(options=options, use_subprocess=True, headless=True,
                     executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
    driver.set_window_size(1920, 1200)
    driver.get("https://shopee.vn")
    driver.forward()
    response = driver.execute_script("var xhr = new XMLHttpRequest();" +
                                     "xhr.open('GET', 'https://shopee.vn/api/v4/shop/rcmd_items?bundle=shop_page_category_tab_main&limit=30&offset=0&shop_id=111138057&sort_type=1&upstream=', false);" +
                                     "xhr.setRequestHeader('Content-Type', 'application/json');" +
                                     "xhr.send();" +
                                     "return xhr.responseText;")
    print("response =  " + response)
    return response


crawl_data_edge()
