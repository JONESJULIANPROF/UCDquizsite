from selenium import webdriver 

import requests

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
        self.browser.get('http://localhost:8000/page1.html')
        self.browser.find_element_by_id("page1Anchor").click()
        self.assertIn('Question 1', self.browser.title, 'Wrong title')
    
    def testPage2NavBar(self):
        self.browser.get('http://localhost:8000/page1.html')
        self.browser.find_element_by_id("page2Anchor").click()
        self.assertIn('Question 2', self.browser.title, 'Wrong title')

    def testHomeFooter(self):
        self.browser.get('http://localhost:8000')
        footer = self.browser.find_element_by_id("footerText")
        self.assertIn('Page By Julian Jones', footer.text, 'Text not found')

    def testPage1Footer(self):
        self.browser.get('http://localhost:8000/page1.html')
        footer = self.browser.find_element_by_id("footerText")
        self.assertIn('Page By Julian Jones', footer.text, 'Text not found')

    def testPage2Footer(self):
        self.browser.get('http://localhost:8000/page2.html')
        footer = self.browser.find_element_by_id("footerText")
        self.assertIn('Page By Julian Jones', footer.text, 'Text not found')


    def testCssLoads(self):
        resp = requests.head('http://localhost:8000/static/Darkly.css')
        self.assertEqual(200, resp.status_code, 'css not found')

    def testImage1(self):
        resp = requests.head('http://localhost:8000/static/Wave.png')
        self.assertEqual(200, resp.status_code, 'img not found')
    
    def testImage2(self):
        resp = requests.head('http://localhost:8000/static/Skull.png')
        self.assertEqual(200, resp.status_code, 'img not found')

    def testImage3(self):
        resp = requests.head('http://localhost:8000/static/CheckMark.png')
        self.assertEqual(200, resp.status_code, 'img not found')

    

if __name__ == '__main__':
    unittest.main()
