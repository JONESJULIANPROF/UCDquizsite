from selenium import webdriver

import unittest

class FunctionalTest(unittest.TestCase):
    global str

    def setUp(self):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.headless=True

        self.browser = webdriver.Chrome(options=chromeOptions)
        self.browser.get('http://localhost:8000')


    def testTitleHome(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Home', self.browser.title, 'Wrong title')

    
    def testTitlePage1(self):
        self.browser.get('http://localhost:8000/page1.html')
        self.assertIn('Question 1', self.browser.title, 'Wrong title')

    


if __name__ == '__main__':
    unittest.main()
