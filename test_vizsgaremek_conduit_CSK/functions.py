# importok?

# bejelentkezéshez:
def login(browser):
    sign_in_btn = self.browser.find_element(By.LINK_TEXT, 'Sign in')
    sign_in_btn.click()

    email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
    password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')

    email_input.send_keys("tesztkitti@teszt.com")
    password_input.send_keys("Teszt123")

    sign_in_btn2 = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_btn2.click()