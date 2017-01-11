import config
import logging
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

log_format = "%(asctime)s %(name)s [%(levelname)s] %(message)s"
logging.basicConfig(format=log_format, filename='horizon.log',
                    level=logging.ERROR)


class BaseSetup(object):

    def base(self):
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

            service_args = ['--ignore-ssl-errors=true', '--ssl-protocol=any']
            self.driver = webdriver.PhantomJS(service_args=service_args)

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
            # self.driver = webdriver.Firefox()

            """
            This will create the session within which all actions take place
            """
            # self.driver.set_window_size(1920, 1080)
            self.driver.maximize_window()
            conf = config.app['horizon']
            user = conf['username']
            passwd = conf['horizon_password']
            ext_vip = conf['external_lb_vip_address']
            url = "https://{0}/".format(ext_vip)
            self.driver.get(url)
            userbox = self.driver.find_element_by_id('id_username')
            passbox = self.driver.find_element_by_id('id_password')
            userbox.send_keys(user)
            passbox.send_keys(passwd)
            self.driver.find_element_by_id('loginBtn').submit()
            # time.sleep(1)
            """
            element is used to ensure the page has fully
            loaded before we start accessing the page elements
            """
            element = WebDriverWait(self.driver, 10).until(
                ec.text_to_be_present_in_element((By.CSS_SELECTOR, "h1"),
                                                 "Projects")
                )
            # time.sleep(5)
        except Exception, e:
            self.driver.save_screenshot('setup.png')
            logging.error(
                "Setup failed... {}".format(e), exc_info=True)
            raise