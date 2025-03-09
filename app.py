import streamlit as st

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    chrome_service = Service(ChromeDriverManager(driver_version="120.0.6099.224").install())

    return webdriver.Chrome(service=chrome_service, options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()
driver.get('http://example.com')

st.code(driver.page_source)