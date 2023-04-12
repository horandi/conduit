from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from adatok import user, article

# bejelentkezéshez:
def login(browser):
    time.sleep(2)
    sign_in_btn = browser.find_element(By.LINK_TEXT, 'Sign in')
    sign_in_btn.click()

    email_input = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
    password_input = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')

    email_input.send_keys(user['email'])
    password_input.send_keys(user['password'])

    sign_in_btn2 = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_btn2.click()
    time.sleep(2)

# cikk módosításhoz...

def new_article(browser):
    new_article_btn = browser.find_element(By.XPATH, '//a[@href="#/editor"]')
    new_article_btn.click()

    article_title = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))
    article_about = browser.find_element(By.XPATH, '//input[@placeholder="What\'s this article about?"]')
    article_text = browser.find_elements(By.XPATH,
                                              '//textarea[@placeholder="Write your article (in markdown)"]')
    article_tags = browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
    publish_article_btn = browser.find_element(By.XPATH, '//button[@type="submit"]')

    article_title.send_keys(article["title"])
    article_about.send_keys(article["about"])
    article_text.send_keys(article["text"])
    article_tags.send_keys(article["tags"])
    publish_article_btn.click()
