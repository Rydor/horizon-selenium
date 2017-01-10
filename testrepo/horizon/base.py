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


class HorizonBase(unittest.TestCase):

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
            self.driver.set_window_size(1920, 1080)
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

    def test_login(self):
        title = self.driver.title
        self.assertIn('Projects - OpenStack Dashboard', title)

    def test_sidebar(self):
        try:
            project_panel = self.driver.find_element_by_css_selector('a[href="#sidebar-accordion-project"]')
            admin_panel = self.driver.find_element_by_css_selector('a[href="#sidebar-accordion-admin"]')
            identity_panel = self.driver.find_element_by_css_selector('a[href="#sidebar-accordion-identity"]')
            #developer_panel = self.driver.find_element_by_css_selector('a[href="#sidebar-accordion-developer"]')
            panels = [project_panel, admin_panel, identity_panel]
            for i in panels:
                i.click()
                if i == project_panel:
                    self.assertIn("Project", i.text)
                elif i == admin_panel:
                    self.assertIn("Admin", i.text)
                elif i == identity_panel:
                    self.assertIn("Identity", i.text)
                elif i == developer_panel:
                    self.assertIn("Developer", i.text)
                else:
                    print "Unhandled use case"
        except Exception, e:
            self.driver.save_screenshot('sidebar.png')
            logging.error(
                "Sidebar test failed... {}".format(e), exc_info=True)
            raise

    def test_create_instance(self):
        try:
            self.driver.find_element_by_css_selector('a[href="#sidebar-accordion-project"]').click()
            time.sleep(2)
            self.driver.find_element_by_css_selector('a[href="/project/instances/"]').click()
            self.driver.find_element_by_id('instances__action_launch').click()
            time.sleep(10)
            self.driver.find_element_by_id("id_name").send_keys('ryan')
            select = Select(self.driver.find_element_by_id('id_source_type'))
            select.select_by_value('image_id')
            select2 = Select(self.driver.find_element_by_id('id_image_id'))
            select2.select_by_index(1)
            self.driver.find_element_by_class_name("btn-primary").submit()
            element = WebDriverWait(self.driver, 60).until(
                ec.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.ajax-update"),
                                                 "Running"))
            """
            Uncomment self.driver.save_screenshot('good.png') in order to
            troubleshoot instance creation errors.
            """
            # self.driver.save_screenshot('good.png')
        except Exception, e:
            self.driver.save_screenshot('create_instance.png')
            logging.error(
                "Instance creation test failed... {}".format(e), exc_info=True)
            raise

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
