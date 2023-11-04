import time

import undetected_chromedriver as uc


# ...
# ...
class Crawl:
    def crawl_data(self):
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        user_profile_path = r'	C:\Users\Admin\AppData\Local\Google\Chrome\User Data'
        options.add_argument(f'user-data-dir={user_profile_path}')
        options.add_argument(f'profile-directory=Profile 21')
        options.add_argument("--disable-gpu")

        driver = uc.Chrome(options=options)

        driver.get("https://shopee.vn")
        time.sleep(2)

        response = driver.execute_script("""
        var xhr = new XMLHttpRequest();
         xhr.open('GET', 'https://shopee.vn/api/v4/shop/rcmd_items?bundle=shop_page_category_tab_main&limit=30&offset=0&shop_id=111138057&sort_type=1&upstream=', false);
         xhr.setRequestHeader('Content-Type', 'application/json');
         xhr.send()
         xhr.responseText
        """)
        print("response =  " + response)

        return response
