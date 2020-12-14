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

    def testHomeNavBar(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_id("homeAnchor").click()
        self.assertIn('Home', self.browser.title, 'Wrong title')
    
    def testPage1NavBar(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_id("page1Anchor").click()
        self.assertIn('Question 1', self.browser.title, 'Wrong title')

    '''def testHomeFooter(self):
        self.browser.get('http://localhost:8080')
        footer = self.browser.find_element_by_id("footerText")
        self.assertIn('Page By Julian Jones', footer, 'Text not found')

    def testPage1Footer(self):
        self.browser.get('http://localhost:8080/page1.html')
        footer = self.browser.find_element_by_id("footerText")
        self.assertIn('Page By Julian Jones', footer, 'Text not found')'''



if __name__ == '__main__':
    unittest.main()
