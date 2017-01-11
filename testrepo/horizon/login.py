import config
import logging
import time
import unittest
from pages.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class LoginTests(unittest.TestCase):

    def setUp(self):
        try:
            """
            This is used to test remotely and through Jenkins.
            Ensure when committing code that this value is not commented out.
            """
            # self.driver = webdriver.PhantomJS()

            """
            :service_args: configuration management for phantomjs
             This is used for testing headless and locally.
            """
            # service_args = ['--proxy=localhost:9999', '--proxy-type=socks5'

            # service_args = ['--ignore-ssl-errors=true', '--ssl-protocol=any']
            # self.driver = webdriver.PhantomJS(service_args=service_args)

            """
            FIREFOX
            The next few lines are needed if you want to execute
            tests in firefox for the visual display of the tests.
            """
            # myProxy = "localhost:9999"
            # proxy = Proxy({
            #     'proxyType': ProxyType.MANUAL,
            #     'socksProxy': myProxy
            # })
            # caps = DesiredCapabilities.FIREFOX
            # caps["marionette"] = True
            # self.driver = webdriver.Firefox(proxy=proxy)
            # self.driver = webdriver.Firefox(capabilities=caps)
            self.driver = webdriver.Firefox()

            """
            This will create the session within which all actions take place
            """
            # self.driver.set_window_size(1920, 1080)
            self.driver.maximize_window()
            conf = config.app['horizon']
            self.user = conf['username']
            self.passwd = conf['horizon_password']
            ext_vip = conf['external_lb_vip_address']
            url = "https://{0}/".format(ext_vip)
            self.driver.get(url)

        except Exception, e:
            self.driver.save_screenshot('setup.png')
            logging.error(
                "Setup failed... {}".format(e), exc_info=True)
            raise

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.login(username=self.user, password=self.passwd)
        title = self.driver.title
        self.assertIn('Projects - OpenStack Dashboard', title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
