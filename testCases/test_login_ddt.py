import pytest
from pageObjects.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.xl_utils import xl
import time

class Test_002_DDT_Login():
    baseURL = ReadConfig.get_base_url()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = xl.getRowCount(self.path, 'Sheet1')
        print('Number of rows...',self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=xl.readData(self.path,'Sheet1',r,1)
            self.password = xl.readData(self.path, 'Sheet1', r, 2)
            self.exp = xl.readData(self.path, 'Sheet1', r, 3)

            self.lp.set_login_username(self.user)
            self.lp.set_login_password(self.password)
            self.lp.click_login_button()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info("**** passed ****")
                    self.lp.click_logout_button()
                    lst_status.append("Pass")
                elif self.exp=='Fail':
                    self.logger.info("**** failed ****")
                    self.lp.click_logout_button()
                    lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")