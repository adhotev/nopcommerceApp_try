from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import pytest


# ddt = Data Driven Testing (DDT)
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = './/TestData/logindata.xlsx'

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_DDT(self, setup):
        self.logger.info('************** Test_002_DDT_Login **************')
        self.logger.info('************** Verifying Login_DDT Test **************')
        driver = setup
        driver.implicitly_wait(10)
        driver.get(self.baseURL)
        lp = LoginPage(driver)

        rows = ExcelUtils.getRowCount(self.path,'Sheet1')
        print('Number of rows in Excel', rows)
        # columns = ExcelUtils.getColumnCount(self.path,sheetName='Sheet1')
        # print('Number of columns in an Excel', columns)

        lst_status = []
        print(lst_status)

        # range starting from 2 as 1st row is header
        for r in range(2, rows + 1):
            username = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.Passed = ExcelUtils.writeData(self.path, 'Sheet1', r, 4, 'Pass')
            self.Failed = ExcelUtils.writeData(self.path, 'Sheet1', r, 4, 'Fail')

            lp.setUserName(username)
            lp.setPassword(password)
            lp.clickLogin()

            act_title = driver.title
            exp_title = 'Dashboard / nopCommerce administration' 
            # always put correct title of page else test will fail
            # as it won't be able to log out from first login

            if act_title == exp_title:
                if exp == 'pass':
                    self.logger.info('************** Passed **************')
                    self.logger.info('************** logging out **************')
                    lp.clickLogout()
                    self.logger.info('************** logged out **************')
                    lst_status.append('Pass')
                    ExcelUtils.writeData(self.path, 'Sheet1', r, 4, 'Pass')
                    # self.Passed

                elif exp == 'fail':
                    self.logger.info('************** Failed **************')
                    lp.clickLogout()
                    lst_status.append('Fail')
                    ExcelUtils.writeData(self.path, 'Sheet1', r, 4, 'Fail')
                    # self.Failed

            elif act_title != exp_title:
            # else:
                if exp == 'fail':
                    self.logger.info('************** Passed **************')
                    lst_status.append('Pass')
                    ExcelUtils.writeData(self.path, 'Sheet1', r, 4, 'Pass')
                    # self.Passed
                elif exp == 'pass':
                    self.logger.info('************** Failed **************')
                    lst_status.append('Fail')
                    ExcelUtils.writeData(self.path, 'Sheet1', r, 4, 'Fail')
                    # self.Failed

        print(lst_status)

        if 'Fail' not in lst_status:
            self.logger.info('************** Login_DDT Test Passed **************')
            driver.close()
            assert True
        else:
            self.logger.info('************** Login_DDT Test Failed **************')
            driver.close()
            assert False

        self.logger.info('************** End of Login_DDT Test **************')
        self.logger.info('************** Completed Test_002_DDT_Login **************')
