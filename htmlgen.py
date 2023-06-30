from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

def get_dom(url):
    firefox_options=Options()
    firefox_options.add_argument("--headless")
    driver=webdriver.Firefox(options=firefox_options)
    driver.get(url)
    return driver

if __name__ == "__main__":
    dom=get_dom("https://www.getyourguide.es/peru-l168997?p=2")
    time.sleep(2)
    with open('sample.html','w') as f:
        f.write(dom.page_source)
