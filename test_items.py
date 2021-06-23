import pytest
from selenium import webdriver

def test__should_see_add_button(browser):
    browser.find_element_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert True, 'Add to basket button does not exit'