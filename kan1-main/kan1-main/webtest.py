import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_title_if_correct(driver):
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    assert "No results found." not in driver.page_source

def test_bgcolor_is_correct(driver):
    driver.get("http://www.python.org")
    elem = driver.find_element(By.CSS_SELECTOR, "div.top-bar").value_of_css_property("background-color")
    assert "rgba(30, 41, 51, 1)" in elem
