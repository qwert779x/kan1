import unittest
from os.path import split


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def test_bgcolor(self):
        driver = self.driver
        driver.get("http://www.python.org")
        elem = driver.find_element(By.CSS_SELECTOR, "div.top-bar").value_of_css_property("background-color")
        print("TextColor of the Element: " + elem)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()