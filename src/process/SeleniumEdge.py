from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service


class ShopeeSeleniumEdge:
    def crawl_data_edge(self):
        options = Options()
        options.add_argument("--window-size=800,600")
        user_profile_path = r'C:\Users\Admin\AppData\Local\Microsoft\Edge\User Data'
        options.add_argument(f'user-data-dir={user_profile_path}')
        options.add_argument(f'profile-directory=Profile 1')
        service = Service()
        driver = webdriver.Edge(options=options)
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
