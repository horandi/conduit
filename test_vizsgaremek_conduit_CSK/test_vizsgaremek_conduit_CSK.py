from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from adatok import user

class TestConduit(object): #Böngésző és az adott oldal megnyitása, bezárása
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

    def teardown_method(self):
        self.browser.quit()

# 1. Adatkezelési nyilatkozat elfogadásának ellenőrzése:
    def test_cookies(self):
        decline_btn = self.browser.find_element(By.XPATH,'//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--decline"]')
        accept_btn = self.browser.find_element(By.XPATH, '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')
        cookie_panel = self.browser.find_element(By.XPATH, '//div[@class="cookie cookie__bar cookie__bar--bottom-left"]')

        assert cookie_panel.is_displayed()
        assert decline_btn.is_enabled()
        assert accept_btn.is_enabled()

        accept_btn.click()

        ### assert not cookie_panel.is_displayed() nem fut le
        ### assert not accept_btn.is_displayed()

# 2. Regisztráció folyamata helyes adatokkal:
    def test_registration(self):
        sign_up_btn = self.browser.find_element(By.LINK_TEXT, 'Sign up')
        sign_up_btn.click

        assert browser.current_url != "http://localhost:1667/#/" # annak ellenőrzése, hogy az URL megváltozik azaz új oldalra visz kattintásra
        time.sleep(2)

        username_input = self.browser.find_element(By.XPATH,'//input[@placeholder="Username"]')
        email_input = self.browser.find_element(By.XPATH,'//input[@placeholder="Email"]')
        password_input = self.browser.find_element(By.XPATH,'//input[@placeholder="Password"]')
        sign_up_reg_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        time.sleep(2)

        username_input.send_keys(user['name'])
        email_input.send_keys(user['email'])
        password_input.send_keys(user['password'])

        sign_up_reg_btn.click()

        reg_message_big = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
        reg_message_small = self.browser.find_element(By.XPATH, '//div[@class="swal-text"]')

        assert reg_message_big.text == 'Welcome'
        assert reg_message_small.text == 'Your registration was successful!'

        reg_ok_btn = self.browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
        reg_ok_btn.click()
        time.sleep(2)
        logut_btn = self.browser.find_element(By.XPATH, '//a[@class="nav-link"]')

        assert logut_btn.is_enabled()
        logut_btn.click()

# 3. Bejelentkezés ellenőrzése helyes adatokkal

    def test_login(self):
        sign_in_btn = self.browser.find_element(By.LINK_TEXT, 'Sign in')
        sign_in_btn.click()

        email_input = self.browser.find_element(By.XPATH,'//input[@placeholder="Email"]')
        password_input = self.browser.find_element(By.XPATH,'//input[@placeholder="Password"]')
        email_input.send_keys(user['email'])
        password_input.send_keys(user['password'])

        sign_in_btn2 =  self.browser.find_element(By.XPATH,'//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_in_btn2.click()

        profile_name_btn = self.browser.find_element(By.XPATH, '//a[@href="#/[name]"]')  # adott usernek a neve az adatok-ból, milyen zárójel kell?
        assert profile_name_btn.is_displayed()

# 4. Adatok listázásának ellenőrzése:

# 5. Több oldalas lista bejárásának ellenőrzése:

    def test_list_of_pages(self):

        page_number_btns = self.browser.find_element(By.XPATH, '//a[@class="page-link"]')
        # for page in page_number_btns:
            page.click()
            active_page = self.browser.find_element(By.XPATH, '//li[@class="page-item active"]')

# 6. Új adatbevitel ellenőrzése:

# 7. Ismételt és sorozatos adatbevitel ellenőrzése adatforrásból:

# 8. Meglévő adat módosításának ellenőrzése:

# 9. Adat törlésének ellenőrzése:

# 10. Adatok lementésének ellenőrzése:

# 11. Kijelentkezés folyamatának ellenőrzése:















