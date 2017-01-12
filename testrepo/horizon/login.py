import basesetup
import unittest
from pages.loginpage import LoginPage


class LoginTests(unittest.TestCase, basesetup.BaseSetup):

    def setUp(self):
        self.login_no_credentials()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.login(username=self.user, password=self.passwd)
        title = self.driver.title
        self.assertIn('Projects - OpenStack Dashboard', title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
