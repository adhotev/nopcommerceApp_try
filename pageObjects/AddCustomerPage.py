from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer():
    # add customer page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    # check-box_Istaxexempt_xpath = "//input[@id='IsTaxExempt']"
    txtcustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    IstitemRegistered_xpath = "//li[normalize-space()='Registered']"
    lstitemAdministrators_xpath = "//li[normalize-space()='Administrators']"
    lstitemGuests_xpath = "//li[normalize-space()='Guests']"
    lstitemVendors_xpath = "//li[@id='bea0b082-44b8-4e2d-8cd4-024d525b5efc']"
    drpmgrofVendor_xpath = "//select[@id='VendorId']"
    # check-box_Active_xpath= "//input[@id='Active']"
    # txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    txtAdminContent_ID = "AdminComment"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def ClickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def ClickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def ClickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Male':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, companyname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(companyname)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.IstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.IstitemRegistered_xpath)

        # self.listitem.click() # as it is not working here use diff method
        self.driver.execute_script("arguments[0].click();", self.listitem)
        # want to set multiple roles call this method multiple times

    def setManagerOfVendor(self, value):
        drp = self.driver.find_element(By.XPATH, self.drpmgrofVendor_xpath)
        drp = Select(drp)
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        # self.driver.find_element(By.XPATH,self.txtcustomerRoles_xpath).send_keys(content)
        self.driver.find_element(By.ID, self.txtAdminContent_ID).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
