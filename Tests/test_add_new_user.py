from selenium import webdriver
import unittest
from Elektrowiz.page_objects.administration_page import UserMenagement
from time import sleep

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.elektrowiz.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test001_CreateNewUser(self):

        UserMenagement.log_in(self)
        UserMenagement.administration_page(self)
        UserMenagement.users_page(self)
        UserMenagement.create_new_user(self)
        sleep(2)
        UserMenagement.check_new_user_msg(self)
        UserMenagement.check_new_user(self)

    def test002_DeleteNewUser(self):

        UserMenagement.log_in(self)
        UserMenagement.administration_page(self)
        UserMenagement.users_page(self)

        UserMenagement.delete_user(self)
        sleep(2)
        UserMenagement.check_del_user_msg(self)
        UserMenagement.check_del_user(self)

    def tearDown(self):
        self.driver.quit()