# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False}, firefox_binary="D:/firefox/esr/firefox.exe")
        self.wd.implicitly_wait(60)
    
    def open_home_page(self, wd) :
        wd.get("http://localhost/addressbook/")
    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_groups_page(self, wd):
		wd.find_element_by_link_text("groups").click()
    def create_group(self, wd, name, header, footer):
        wd.find_element_by_name("new").click()

        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        
        wd.find_element_by_name("submit").click()
    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def logout(self,wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        success = True
        wd = self.wd

        self.open_home_page(wd)

        self.login(wd,username="admin", password="secret")
        
        self.open_groups_page(wd)
		
        self.create_group(wd, name="test_group", header="test_group_header", footer="test_group_footer")
        self.return_to_group_page(wd)

        self.logout(wd)
        
    def test_add_empty_group(self):
        success = True
        wd = self.wd

        self.open_home_page(wd)

        self.login(wd,username="admin", password="secret")
        
        self.open_groups_page(wd)
		
        self.create_group(wd, name="", header="", footer="")
        self.return_to_group_page(wd)

        self.logout(wd)
    
        
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
