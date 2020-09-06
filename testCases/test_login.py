import pytest
from selenium import webdriver
from pageObjects.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.driver = setup
        self.logger.info("******** Test_001_Login --> test_homepage_title ********")
        self.driver.get(self.baseURL)
        actual_homepage_title = self.driver.title

        if actual_homepage_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******** Test_001_Login --> test_homepage_title --> PASSED ********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            self.logger.error("******** Test_001_Login --> test_homepage_title --> FAILED ********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.logger.info("******** Test_001_Login --> test_login ********")
        self.driver.get(self.baseURL)

        self.login_page_obj = LoginPage(self.driver)
        self.login_page_obj.set_login_username(self.username)
        self.login_page_obj.set_login_password(self.password)
        self.login_page_obj.click_login_button()

        actual_loginpage_title = self.driver.title
        if actual_loginpage_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("******** Test_001_Login --> test_login --> PASSED ********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("******** Test_001_Login --> test_login --> FAILED ********")
            assert False
