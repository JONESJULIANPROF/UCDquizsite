from django.test import TestCase
from django.urls import resolve
from UCDquizApp.views import home_page
from UCDquizApp.views import page1_page
from UCDquizApp.views import page2_page


from django.http import HttpRequest


class ProgramTest(TestCase):
    def testHomePage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page, "Home is bad")
    
    def testPage1Page(self):
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
        self.assertIn('<button type="submit" class="btn btn-primary" id="submit" onclick="storeChoice()">Store your choice!</button>', html, 'it broke')
    def testHomePageNavContext1(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<nav class="navbar navbar-expand-lg navbar-dark bg-dark">', html, 'it broke')
    
    def testHomePageNavContext2(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<a class="nav-link" href="home.html" id="homeAnchor">Home</a>', html, 'it broke')

    def testHomePageNavContext3(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<a class="nav-link" href="page1.html" id="page1Anchor">Question 1</a>', html, 'it broke')
    
    def testHomePageNavContext4(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<a class="nav-link" href="page2.html" id="page2Anchor">Question 2</a>', html, 'it broke')

    def testPage1NavContext1(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<nav class="navbar navbar-expand-lg navbar-dark bg-dark">', html, 'it broke')
    
    def testPage1NavContext2(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<a class="nav-link" href="home.html" id="homeAnchor">Home</a>', html, 'it broke')

    def testPage1NavContext3(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<a class="nav-link" href="page1.html" id="page1Anchor">Question 1</a>', html, 'it broke')

    def testPage1NavContext4(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<a class="nav-link" href="page2.html" id="page2Anchor">Question 2</a>', html, 'it broke')
    def testPage1Img(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<img id="outputImg" alt="Image" title="Image">', html, 'it broke')
    def testPage1Output(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<h2 id="outputText"></h2>', html, 'it broke')
    def testPage1Label(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<label for="inputBox">There is a strange glass on the table, do you take it?</label>', html, 'it broke')
    def testPage1Input(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="text" id="inputBox">', html, 'it broke')
    
    def testPage1Input(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<button type="submit" class="btn btn-primary" id="submit" onclick="storeChoice()">Store your choice!</button>', html, 'it broke')

    def testPage1Input(self):
        request = HttpRequest()
        response = page1_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<button type="submit" class="btn btn-primary" id="submit" onclick="storeChoice()">Store your choice!</button>', html, 'it broke')

    
    def testPage2NavContext1(self):
        request = HttpRequest()
        response = page2_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<nav class="navbar navbar-expand-lg navbar-dark bg-dark">', html, 'it broke')
    
    def testPage2NavContext2(self):
        request = HttpRequest()
        response = page2_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<a class="nav-link" href="home.html" id="homeAnchor">Home</a>', html, 'it broke')

    def testPage2NavContext3(self):
        request = HttpRequest()
        response = page2_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<a class="nav-link" href="page1.html" id="page1Anchor">Question 1</a>', html, 'it broke')
    
    def testPage2NavContext4(self):
        request = HttpRequest()
        response = page2_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<a class="nav-link" href="page2.html" id="page2Anchor">Question 2</a>', html, 'it broke')

    def testPage2H1(self):
        request = HttpRequest()
        response = page2_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1 id="banner"></h1>', html, 'it broke')

    
    def testPage2Label(self):
        request = HttpRequest()
        response = page2_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<label for="inputBox">You escape the room, and get the opportunity to kill an unsuspecting guard. Do you?</label>', html, 'it broke')

    def testPage2Input(self):
        request = HttpRequest()
        response = page2_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<input type="text" id="inputBox">', html, 'it broke')
    
    def testPage2Button(self):
        request = HttpRequest()
        response = page2_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<button type="submit" class="btn btn-primary" id="submit" onclick="storeChoice()">Store your choice!</button>', html, 'it broke')

    def testPage2Img(self):
        request = HttpRequest()
        response = page2_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<img id="outputImg" alt="Image" title="Image">', html, 'it broke')

    def testPage2Footer(self):
        request = HttpRequest()
        response = page2_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<p class="text-muted" id="footerText">Page By Julian Jones</p>', html, 'it broke')





    


    
    
    


    
    

    

    
    
    




# Create your tests here.


