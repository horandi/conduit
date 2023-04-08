import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from adatok import user

service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

URL = "http://localhost:1667/#/"
browser.get(URL)
#browser.maximize_window()


cookie_panel = browser.find_element(By.XPATH, '//div[@class="cookie cookie__bar cookie__bar--bottom-left"]')
accept_btn = browser.find_element(By.XPATH, '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')
assert cookie_panel.is_displayed()
assert accept_btn.is_displayed()

#accept_btn.click()

sign_up_btn = browser.find_element(By.LINK_TEXT, 'Sign up')
sign_in_btn = browser.find_element(By.LINK_TEXT, 'Sign in')

sign_up_btn.click()
# get_url = browser.current_url
assert browser.current_url != "http://localhost:1667/#/"




# time.sleep(1)
# username_input = browser.find_element(By.XPATH,'//input[@placeholder="Username"]')
# email_input = browser.find_element(By.XPATH,'//input[@placeholder="Email"]')
# password_input = browser.find_element(By.XPATH,'//input[@placeholder="Password"]')
# sign_up_reg_btn = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
#
# username_input.send_keys(user['name'])
# email_input.send_keys(user['email'])
# password_input.send_keys(user['password'])
# sign_up_reg_btn.click()
# time.sleep(2)
# reg_message = browser.find_element(By.XPATH, '//div[@class="swal-title"]')
# time.sleep(2)
# reg_ok_btn = browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
# reg_ok_btn.click()
# time.sleep(2)
# logut_btn = browser.find_element(By.XPATH, '//a[@class="nav-link"]')
# assert logut_btn.is_enabled()