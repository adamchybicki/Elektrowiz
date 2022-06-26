from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from credentials import LoginVariables
from time import sleep

class Variables():
    newusrlogin = "jkowalski"
    newusrpsswd = "1234abcd"
    newusrname = "Jan"
    newuserlastname = "Kowalski"
    newusremail = "jkowalski@test.com"
    company = "Niedzica"
    usractive = "TAK"
    usrstatus = "zweryfikowane"

class UserMenagement():
    login = "login"
    password = "password"
    login_btn = "Login"
    administration = "Panel administracyjny"
    users = "//a[@href='users.php']"
    newuseraddbtn = "//img[@data-target='#user_add']"
    newuserlogininput = "user_login"
    newuserpasswdinput = "user_password"
    newusernameinput = "user_name"
    newuserlastnameinput = "user_lastname"
    newusercompanyselect = "user_affiliation"
    newuseremail = "user_email"
    newuseractivation = "user_active"
    newuserstatus = "user_status"
    savebtn = "submit"
    newusermsg = "//div[@class='message_box' and text()='Konto zostało stworzone']"
    closebtn = "//td//button[text()='Zamknij']"
    newuserlogin = "//table[@id='user_list']//td[text()='" + Variables.newusrlogin + "']"
    deletebtn = "//tr/td[text()='" + Variables.newusrlogin + "']/following-sibling::td/img[@src='images/delete.png']"
    deleteusermsg = "//div[@class='message_box' and text()='Konto użytkownika zostało usunięte.']"
    userslist = "user_list"

    def log_in(self):
        driver = self.driver
        driver.find_element(By.NAME, UserMenagement.login).send_keys(LoginVariables.usrlogin)
        driver.find_element(By.ID, UserMenagement.password).send_keys(LoginVariables.usrpasswd)
        driver.find_element(By.NAME, UserMenagement.login_btn).click()

    def administration_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, UserMenagement.administration).click()

    def users_page(self):
        driver = self.driver
        driver.find_element(By.XPATH, UserMenagement.users).click()

    def create_new_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, UserMenagement.newuseraddbtn).click()
        driver.find_element(By.ID, UserMenagement.newuserlogininput).send_keys(Variables.newusrlogin)
        driver.find_element(By.ID, UserMenagement.newuserpasswdinput).send_keys(Variables.newusrpsswd)
        driver.find_element(By.ID, UserMenagement.newusernameinput).send_keys(Variables.newusrname)
        driver.find_element(By.ID, UserMenagement.newuserlastnameinput).send_keys(Variables.newuserlastname)
        company_select = Select(driver.find_element(By.ID, UserMenagement.newusercompanyselect))
        company_select.select_by_visible_text(Variables.company)
        driver.find_element(By.ID, UserMenagement.newuseremail).send_keys(Variables.newusremail)
        user_active_select = Select(driver.find_element(By.ID, UserMenagement.newuseractivation))
        user_active_select.select_by_visible_text(Variables.usractive)
        user_status_select = Select(driver.find_element(By.ID, UserMenagement.newuserstatus))
        user_status_select.select_by_visible_text(Variables.usrstatus)
        driver.find_element(By.ID, UserMenagement.savebtn).click()

    def check_new_user_msg(self):
        driver = self.driver
        new_user_msg = driver.find_element(By.XPATH, UserMenagement.newusermsg)
        self.assertEqual("Konto zostało stworzone", new_user_msg.text, "There is no message about adding a user")

        driver.find_element(By.XPATH, UserMenagement.closebtn).click()

    def check_new_user(self):
        driver = self.driver
        new_user_check = driver.find_element(By.XPATH, UserMenagement.newuserlogin)
        self.assertEqual(Variables.newusrlogin, new_user_check.text, "There is no new user")

    def delete_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, UserMenagement.deletebtn).click()

    def check_del_user_msg(self):
        driver = self.driver
        new_user_delete_msg = driver.find_element(By.XPATH, UserMenagement.deleteusermsg)
        self.assertEqual("Konto użytkownika zostało usunięte.", new_user_delete_msg.text, "There is no message about user deletion")

    def check_del_user(self):
        driver = self.driver
        bodyText = driver.find_element(By.ID, UserMenagement.userslist)
        self.assertFalse(Variables.newusrlogin in bodyText.text)
