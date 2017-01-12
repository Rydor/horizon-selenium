import basepage


class LoginPage(basepage.BasePage):

    def set_username(self, username):
        userbox = self.driver.find_element_by_id('id_username')
        userbox.send_keys(username)

    def set_password(self, password):
        passbox = self.driver.find_element_by_id('id_password')
        passbox.send_keys(password)

    def click_connect(self):
        self.driver.find_element_by_id('loginBtn').submit()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_connect()
