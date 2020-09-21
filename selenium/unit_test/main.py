import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("/home/jan/code/python/selenium/chromedriver")
        self.driver.get("http://www.python.org")

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
