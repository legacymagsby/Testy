import unittest
from selenium import webdriver
import requests, time
import os


class SeleniumCBT(unittest.TestCase):
    def setUp(self):

        self.username = os.environ['CBT_USERNAME']
        self.authkey = os.environ['CBT_APIKEY']
        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)
        self.test_result = None
        self.hash = None
        self.testId = None
        caps = {}
        caps['record_video'] = 'true'
        caps['browser_api_name'] = os.environ['CBT_BROWSER']
        caps['os_api_name'] = os.environ['CBT_OPERATING_SYSTEM']
        caps['screen_resolution'] = os.environ['CBT_RESOLUTION']
    

        try:
            self.driver = webdriver.Remote(
            desired_capabilities=caps, 
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username, self.authkey))
        except Exception as e:
            raise e
                 
    def test_CBT(self):
            self.driver.maximize_window()
            #self.driver.get("http://google.com")
            self.driver.get("http://10.0.0.11:3000/")
            print("The window size is", self.driver.get_window_size()) #the window size    
            print("the title is",self.driver.title)
            self.driver.quit()
          
           
if __name__ == '__main__':
    unittest.main()


