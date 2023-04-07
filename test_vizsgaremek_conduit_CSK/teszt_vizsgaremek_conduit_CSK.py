from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class TestConduit(object):
    #Böngésző és az adott oldal megnyitása, bezárása
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://localhost:1667/"
        self.browser.get(URL)
        self.browser.maximize_window()

    # def teardown_method(self):
        self.browser.quit()

# Adatkezelési nyilatkozat elfogadásának ellenőrzése:
    def test_cookies(self):
        decline_btn = self.browser.find_element(By.XPATH,'//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--decline"]')
        accept_btn = self.browser.find_element(By.XPATH, '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')

        assert decline_btn.is_enabled()
        assert accept_btn.is_enabled()

        accept_btn.click()

