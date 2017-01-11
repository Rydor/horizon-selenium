import config
import logging
import time
import unittest
import setup
from pages.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class HomePageTest(unittest.TestCase):

    def setUp(self):
        