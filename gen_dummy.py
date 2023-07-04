from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import sys

def get_dom(url):
    firefox_options=Options()
    firefox_options.add_argument("--headless")
    driver=webdriver.Firefox(options=firefox_options)
    driver.get(url)
    return driver

if __name__ == "__main__":
    page=str(sys.argv[1])
    dom=get_dom(page)
    time.sleep(2)
    with open('peru/html/dummy.html','w') as f:
        f.write(dom.page_source)
