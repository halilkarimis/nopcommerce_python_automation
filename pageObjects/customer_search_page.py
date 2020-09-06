import time


class CustomerSearch:
    def __init__(self, driver):
        self.driver = driver

    txt_field_email_xpath = "//input[@id='SearchEmail']"
    txt_field_first_name_id = "//input[@id='SearchFirstName']"
    txt_field_last_name_id = "//input[@id='SearchLastName']"
    btn_search_customer_xpath = "//button[@id='search-customers']"

    rows_table_customer_list = "//table[@id='customers-grid'] //tr/td[2]"
    columns_table_customer_list = "//table[@id='customers-grid'] //tr[1] //td[2]"

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.txt_field_first_name_id).clear()
        self.driver.find_element_by_xpath(self.txt_field_email_xpath).send_keys(email)

    def set_first_name(self, first_name):
        self.driver.find_element_by_xpath(self.txt_field_first_name_id).clear()
        self.driver.find_element_by_xpath(self.txt_field_first_name_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element_by_xpath(self.txt_field_last_name_id).clear()
        self.driver.find_element_by_xpath(self.txt_field_last_name_id).send_keys(last_name)



    def search_email(self, email):
        self.driver.find_element_by_xpath(self.btn_search_customer_xpath).click()
        actual_email = self.driver.find_element_by_xpath(self.rows_table_customer_list).text
        print(actual_email)
        if actual_email == email:
            print("FOUND")
        else:
            print("NOT FOUND")

    def search_first_name(self, customer_name):
        self.driver.find_element_by_xpath(self.btn_search_customer_xpath).click()
        actual_customer_name = self.driver.find_element_by_xpath(self.columns_table_customer_list).text
        print(actual_customer_name)
        if actual_customer_name == customer_name:
            print("FOUND")
            self.driver.close()
        else:
            print("NOT FOUND")
            self.driver.close()
