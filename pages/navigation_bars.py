import basepage


class NavigationBars(basepage.BasePage):

    def click_project_panel(self):
        self.driver.find_element_by_css_selector(
            'a[href="#sidebar-accordion-project"]').click()

    def click_admin_panel(self):
        self.driver.find_element_by_css_selector(
            'a[href="#sidebar-accordion-admin"]').click()

    def click_identity_panel(self):
        self.driver.find_element_by_css_selector(
            'a[href="#sidebar-accordion-identity"]').click()

    def click_developer_panel(self):
        self.driver.find_element_by_css_selector(
            'a[href="#sidebar-accordion-developer"]').click()

    def click_project_compute(self):
        self.driver.find_element_by_css_selector(
            'a[href="#sidebar-accordion-project-compute"]').click()

    def click_project_compute_instance(self):
        self.driver.find_element_by_css_selector(
            'a[href="/project/instances/"]').click()