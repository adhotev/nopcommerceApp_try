from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.vijay
    @pytest.mark.regression
    def test_HomePageTitle(self,setup):

        self.logger.info('************** Test_001_Login **************')
        self.logger.info('************** Verifying HomePage Title **************')
        driver = setup
        driver.get(self.baseURL)
        act_title = driver.title
        if act_title == 'Your store. Login':
            assert True
            driver.close()
            self.logger.info('************** HomePage Title Test Passed **************')
        else:
            driver.save_screenshot('./Screenshots/test_HomePageTitle.png')
            driver.close()
            self.logger.error('************** HomePage Title Test Failed **************')
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info('************** Verifying Login Test **************')
        driver = setup
        driver.get(self.baseURL)
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        act_title = driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            # print(driver.title)
            # lp.clickLogout()
            driver.close()
            self.logger.info('************** Login Test Passed **************')
            assert True
        else:
            driver.save_screenshot('./Screenshots/test_Login.png')
            driver.close()
            self.logger.error('************** Login Test Failed **************')
            assert False
