class AddCustomer:
    def __init__(self, driver):
        self.driver = driver

    menu_link_customers_xpath = "//ul[@class='sidebar-menu tree'] //a[@href='#'] //span[text()='Customers']"
    menu_item_link_customers_xpath = "//a[@ class ='menu-item-link'] //span[text()='Customers']"

    def click_menu_link_customers(self):
        self.driver.find_element_by_xpath(self.menu_link_customers_xpath).click()

    def click_menu_item_link_customers(self):
        self.driver.find_element_by_xpath(self.menu_item_link_customers_xpath).click()
