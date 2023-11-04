import random
import time

import undetected_chromedriver as uc
from selenium import webdriver
from selenium_stealth import stealth

# Khởi tạo undetected_chromedriver
options = webdriver.ChromeOptions()

options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = uc.Chrome(options=options)

#
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

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

    print(driver.execute_script("""
    let res = await fetch("https://shopee.vn/api/v4/shop/rcmd_items?bundle=shop_page_category_tab_main&limit=30&offset=0&shop_id=26947756&sort_type=1&upstream=", {
  "headers": {
    "accept": "application/json",
    "af-ac-enc-dat": "AAczLjEuMC0yAAABi4Teiy0AAA/uAzAAAAAAAAAAAiSDMisSv7k4nlI2p9KZ0MfOD7+o8MS3gD4Lv0cZsWDYYHdpR1c3Np8BzcsRRPm/ZZgFLUngG5gdglPRlokHaBO6riuJzOhSEoCDq8ldg+RcTmGj6lzRcbx+u+wuFArvx+zvDDCzMOdK2xGN7mdKcf0ai/FxzOhSEoCDq8ldg+RcTmGj6lzRcbx+u+wuFArvx+zvDDBGV2Ia3yab8r/0vvuJ/GyfpohFHsEFTkPArlIVDn5bBVRiZeaLJCVJU0SfG5dRLyXEplSWPkm3eMEC3t+KLNlvGAt58mjadOCSqdJGJMljclRiZeaLJCVJU0SfG5dRLyWAfnvbv/x1c/yrtF8pL0PZHvJ7N52r4m0D8jIqw9a6iRBPodmt4EdszHIcF4opk6bA0ZlW/HUmCMddRLP/+20isc2Xbfdc2gpt/+aJUOqVPH+RElVIBn5MeXS/LyLxjKleJMBaI8uVZb5pmqhCKYFWXR0XEHp7nMd/yK6jJfN2mv439vzknrcdleW6J26R8SlgUIRBDXTXr7nYsbBk4Wfdl/82EyfDx/bVRcPaaRvYmx4w4Q2f1+5Ym1/IC107OOcaDPjUDvke9kcCC9qpyKAneVtks1BST6eLSS4Vm6Mzx0gD9O1aYGgjmjuYbekv+r8muLR9q3qwJZNsj+3HLUSw4QT09hTUs0ZKYbLoWrMR+HaJ0btR+xuwDBhKL4RovNCbTIr479Gj605haPeKsybWR166CeSB22O9kryz3KoireVnmNgpqjhtHkglhGmTfBO2GjYJ1wIWmI00eTXcfbEX9GTzuvH6BOF4ICNGcoeF/BUOWnie3o/94l7VW+IxRpT47ZLRC1KF6tLaERdY7vMfZ/Or3A/xSA69kapmUUipQKdHgsmrlEF/4YJtMVWTyedDMC0MfgAdRtDMqQxV1ZZVHiCkfq5o2kIAZeT9Uesjh6fDosrcD659bwu9kUf/OtKX+yIurpSBgrqEApRZVYT8l/82EyfDx/bVRcPaaRvYm9T5zKc7e6z9HwaLc4pqgPB7BFaEPWducFt9td3B+jkm+qbllAwjUJ1rNYEEhZMktIN8LLEO/j8/rtbF7nTQn1o=",
    "af-ac-enc-sz-token": "0AYvU7ZqUBOs6jeMJK0LsQ==|pSVrpSJjt7uO1r7c/9nqC/kcqRD6NU9jEnixRk7PfEjfw0aUn4BhDZgZEfSwdnMqI/KWkwXIwAnGIA==|6KWBoFc7saUxaH0g|08|3",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?0",
    "x-api-source": "pc",
    "x-csrftoken": "8NpDZFJRUcmLvj2qSDULXvEADmO5YvRu",
    "x-requested-with": "XMLHttpRequest",
    "x-sap-ri": "0dbc406548c80ae522a40839010110fda09a92d4aff42251d644",
    "x-sap-sec": "K7Vu9gLPLEtO0EtO2vts0EGO2vtO0EGO0Etr0EtOaEUO0htP0EtI0EtOwr+bFxhO0Etf0/tOBEUO0P/dCU3EipFo7dvjK9sU6uGjPIjVhdHRI+BdCbCM3w80HsfZJ+qoWUUx6ffHpX1L+jmF7CwTmc/VIQdUqqQ+44XEfo+thm2G/NI8wljIrHhU9p3wzC4xgIOHL9/Irc9991QezV1dmvSS4+sW01zsFh/VaThYvuVxsaaCs6GUCba8CLpW9k+27oh23rI5WF3IUDPVz0Ci0D1WiigBDzvAnlGpsDGraGWV/afjVGwqiBttfnWuX/GjbMcQ5thJPGsD+/I610/P5xSZzYMJFXE3jPQW+2aNLY8YLsT32GFiSUlxPouAoVYAiksClnXlw/mwUnkp5Evuqk+Bkda8IqREbWryOIEWrXp7dFP2wZOdNWkf64LzPDsbiTOy52mR3CAv9q3MPU+YsP/kKEtO0HZik6FlQ6gC0EtO0O0bFjcs0EtO3EtO0eGO0EuvcnWNeAvE/UpMr3L37e68dwDVKvhO0EtlQ6lXdbfXRxtO0Ets0ELOKEtI0EhO0Ets0EtO3EtO0eGO0EtF7SnT/hfXRA09sMr/lT/zKEwDpEhO0Etik6UyRqD9R/tO0En=",
    "x-shopee-language": "vi",
    "x-sz-sdk-version": "3.1.0-2&1.5.1"
  },
  "referrer": "https://shopee.vn/unilever_vietnam",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET",
  "mode": "cors",
  "credentials": "omit"
});
return await res.text()
    """))

