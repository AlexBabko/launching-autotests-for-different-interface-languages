import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru/it/de")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    #options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print('language fo bowser:',user_language)
    link = f"http://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/"
    print('link for current site:',link)
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
