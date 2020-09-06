import pytest
import time
from pageObjects.login_page import LoginPage
from pageObjects.add_customer_page import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_Add_Customer:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_add_customer(self, setup):

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        login_page_obj = LoginPage(self.driver)
        login_page_obj.set_login_username(self.username)
        login_page_obj.set_login_password(self.password)
        login_page_obj.click_login_button()

        self.customer_page_obj = AddCustomer(self.driver)
        self.customer_page_obj.click_menu_link_customers()
        self.customer_page_obj.click_menu_item_link_customers()
        actual_title = self.driver.title

        if actual_title == "Customers / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****** Add Customer Passed ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Test_003_Add_Customer.png")
            self.driver.close()
            self.logger.info("********* Add Customer FAILED *****")
            assert False


