import pytest
from pageObjects.login_page import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.customer_search_page import CustomerSearch
from pageObjects.add_customer_page import AddCustomer

class Test_005_Customer_Search:
    baseURL = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_customer_email_search(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        login_page_obj = LoginPage(self.driver)
        login_page_obj.set_login_username(self.username)
        login_page_obj.set_login_password(self.password)
        login_page_obj.click_login_button()

        self.customer_page_obj = AddCustomer(self.driver)
        self.customer_page_obj.click_menu_link_customers()
        self.customer_page_obj.click_menu_item_link_customers()

        self.customer_search_obj = CustomerSearch(self.driver)
        self.customer_search_obj.set_email("victoria_victoria@nopCommerce.com")
        self.customer_search_obj.search_email("victoria_victoria@nopCommerce.com")

        self.customer_search_obj.set_first_name("Victoria")
        self.customer_search_obj.set_last_name("Terces")

        self.customer_search_obj.search_first_name("Victoria Terces")
