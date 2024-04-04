from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest
import string
import random
from faker import Faker

# fake = Faker()


class Test_003_AddCustomer:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************** Test_003_AddCustomer **************")
        driver = setup
        driver.get(self.baseURL)
        driver.maximize_window()

        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************** login successful **************")

        self.logger.info("************** starting add customer test **************")

        addcust = AddCustomer(driver)
        addcust.ClickOnCustomerMenu()
        addcust.ClickOnCustomerMenuItem()
        addcust.ClickOnAddnew()

        self.logger.info("************** providing customer info **************")

        # email = random_generator() + '@gmail.com'
        # addcust.setEmail(email)
        # addcust.setPassword('test123')
        # addcust.setFirstName('avinash')
        # addcust.setLastName('patil')
        # addcust.setGender('Male')
        # addcust.setDob('5/10/1989')
        # addcust.setCompanyName('busyQA')
        # addcust.setCustomerRoles('Guests')
        # addcust.setManagerOfVendor('Vendor 2')
        # self.logger.info("************** running **************")
        # addcust.setAdminContent('This is for Testing.')
        # addcust.clickOnSave()

        # self.fake = Faker()
        #
        # addcust.setEmail(self.fake.email())
        # addcust.setPassword(self.fake.password())
        # addcust.setFirstName(self.fake.first_name())
        # addcust.setLastName(self.fake.last_name())
        # addcust.setGender('Male')
        # addcust.setDob(self.fake.date_of_birth(minimum_age=18,maximum_age=100).strftime('%d/%m/%Y'))
        # addcust.setCompanyName(self.fake.company())
        # addcust.setCustomerRoles('Guests')
        # addcust.setManagerOfVendor('Vendor 2')
        # addcust.setAdminContent(self.fake.text())
        # addcust.clickOnSave()

        fake = Faker()

        addcust.setEmail(fake.email())
        addcust.setPassword(fake.password())
        addcust.setFirstName(fake.first_name())
        addcust.setLastName(fake.last_name())
        addcust.setGender('Male')
        addcust.setDob(fake.date_of_birth(minimum_age=18, maximum_age=100).strftime('%m/%d/%Y'))
        addcust.setCompanyName(fake.company())
        addcust.setCustomerRoles('Guests')
        addcust.setManagerOfVendor('Vendor 2')
        addcust.setAdminContent(fake.text())
        addcust.clickOnSave()

        self.logger.info("************** saving customer info **************")

        self.logger.info("************** add customer validation started **************")

        msg = driver.find_element(By.TAG_NAME,'body').text
        print(msg)

        if 'The new customer has been added successfully.' in msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            driver.save_screenshot("./Screenshots/test_addCustomer_scr.png")
            self.logger.error("******* Add customer Test Failed ************")
            assert False

        driver.close()
        self.logger.info("******* Ending Test_003_AddCustomer Test ******")


# def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for i in range(size))

