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
    dom=get_dom("https://www.getyourguide.com/peru-l168997?p={0}".format(page))
    time.sleep(5)
    with open('peru/html/p{0}.html'.format(page),'w') as f:
        f.write(dom.page_source)
