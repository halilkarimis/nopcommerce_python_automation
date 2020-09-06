from selenium import webdriver


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    # button_login_xpath = "//input[@value='Log in']"
    button_login_xpath = "//input[@class='button-1 login-button']"
    button_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_login_username(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def set_login_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout_button(self):
        self.driver.find_element_by_link_text(self.button_logout_linktext).click()
