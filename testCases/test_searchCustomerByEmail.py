from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time
import pytest


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************** Starting Test_004_SearchCustomerByEmail **************")
        driver = setup
        driver.get(self.baseURL)
        driver.maximize_window()

        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************** login successful **************")

        self.logger.info("************** starting search Customer By Email test **************")

        addcust = AddCustomer(driver)
        addcust.ClickOnCustomerMenu()
        addcust.ClickOnCustomerMenuItem()

        self.logger.info("************** searching Customer By Email **************")
        searchcust = SearchCustomer(driver)
        searchcust.setEmail('steve_gates@nopCommerce.com')
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail('steve_gates@nopCommerce.com')
        assert True == status
        self.logger.info("************** Ending Test_004_SearchCustomerByEmail **************")
        driver.close()
