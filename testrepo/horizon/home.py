import config
import logging
import time
import unittest
import basesetup
from pages.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class HomePageTest(unittest.TestCase, basesetup.BaseSetup):

    def setUp(self):
        self.login_with_credentials()

    def test_sidebar(self):
        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
