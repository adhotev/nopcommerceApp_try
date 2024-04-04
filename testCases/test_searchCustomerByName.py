from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time
import pytest


class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("************** Test_004_SearchCustomer **************")
        driver = setup
        driver.get(self.baseURL)
        driver.maximize_window()

        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************** login successful **************")

        self.logger.info("************** starting search Customer By Name test **************")

        addcust = AddCustomer(driver)
        addcust.ClickOnCustomerMenu()
        addcust.ClickOnCustomerMenuItem()

        self.logger.info("************** searching Customer By Name **************")
        searchcust = SearchCustomer(driver)
        searchcust.setFirstName('Brenda')
        searchcust.setLastName('Lindgren')
        searchcust.clickSearch()
        time.sleep(5)

        status = searchcust.searchCustomerByName('Brenda Lindgren')
        assert True == status
        self.logger.info("************** Ending Test_005_SearchCustomerByName **************")
        driver.close()
