import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/home/jan/code/python/selenium/chromedriver")
        self.driver.get("http://www.python.org")

    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.search_text_element = "pydoc"
        main_page.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
