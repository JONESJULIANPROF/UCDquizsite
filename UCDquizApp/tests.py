from django.test import TestCase
from django.urls import resolve
from UCDquizApp.views import home_page
from UCDquizApp.views import page1_page
from django.http import HttpRequest


class ProgramTest(TestCase):
    def testHomePage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page, "Home is bad")
    
    def testHomePage(self):
        found = resolve('/page1.html')
        self.assertEqual(found.func, page1_page, "page1 is bad")

    def testHomeH1(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1>Welcome Traveler!</h1>', html, 'it broke')
    def testHomeLabel(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<label for="inputBox">What is your name, fair one?</label>', html, 'it broke')
    def testHomeInput(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="text" id="inputBox">', html, 'it broke')
    def testHomeButton(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<button id="submit" type="submit" onclick="storeName()">Submit!</button>', html, 'it broke')
    def testHomeP(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<p id="output"></p>', html, 'it broke')

    def testPageH1(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1 id="banner"></h1>', html, 'it broke')
    
    def testPageLabel(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<label for="inputBox">There is a strange glass on the table, do you take it?</label>', html, 'it broke')
    
    def testPageInput(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="text" id="inputBox">', html, 'it broke')
    def testPageButton(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<button type="submit" id="submit">Submit!</button>', html, 'it broke')
    
    




# Create your tests here.


