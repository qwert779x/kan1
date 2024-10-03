import unittest
from os.path import split


from selenium import webdriver
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# TODO: Dodanie pliku gitignore w celu zignorowania niepotrzebnych plików
# Zmienienie sposobu intrakcji na bloki ActionChains dla poprawienia czytelności kodu. Przykład:
# ActionChains(self.driver)\
#     .move_to_element(elem)\
#     .send_keys("pycon")\
#     .key_down(Keys.RETURN)\
#     .perform()
# ActionBuilder.clear_actions()
# self.assertNotIn("No results found.", driver.page_source)

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
