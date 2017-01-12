import unittest
import basesetup
from pages.navigation_bars import NavigationBars


class NavBarTest(unittest.TestCase, basesetup.BaseSetup):

    def setUp(self):
        self.login_with_credentials()

    def test_project_panel(self):
        session = NavigationBars(self.driver)
        session.click_project_panel()
        self.assertIn("sidebar-accordion-project", self.driver.current_url)

    def test_admin_panel(self):
        session = NavigationBars(self.driver)
        session.click_admin_panel()
        self.assertIn("sidebar-accordion-admin", self.driver.current_url)

    def test_identity_panel(self):
        session = NavigationBars(self.driver)
        session.click_identity_panel()
        self.assertIn("sidebar-accordion-identity", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()