import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class SearchTests(unittest.TestCase):
    def setUp(self):
        #	create	a	new	Firefox	session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        #	navigate	to	the	application	home	page
        self.driver.get("https://www.etwinning.net/pl/pub/index.htm")

    def test_register(self):
        driver = self.driver
        # click	on	Log	In/register	link	to	open	Login/register	page
        driver.find_element_by_xpath("/html/body/div/header/div[3]/div[2]/div/div[2]/button/span").click()
        # get register link
        create_preregister_button = driver.find_element_by_xpath(
            "body > div > header > div.login-popup > div > a").click()
        #	check preregister button	is	displayed	and	enabled
        self.assertTrue(create_preregister_button.is_displayed() and create_preregister_button.is_enabled())
        # click on preregister button
        create_preregister_button.click()
        #	get	all	the	fields	from	Create	an	Account	form
        first_name = driver.find_element_by_name("firstname")
        last_name = driver.find_element_by_name("lastname")

        #Select element from list
        country = driver.find_element_by_xpath("//select[@name='name']")
        all_options = country.find_elements_by_name("country")
        for option in all_options:
        print("Value is: %s" % option.get_attribute("616"))
        option.click()
        country = driver.select

        email_adress = driver.find_element_by_name("email")
        re_type_email = driver.find_element_by_name("email2")
        choose_username = driver.find_element_by_name("username")
        choose_password = driver.find_element_by_name("password")
        re_type_password = driver.find_element_by_name("password2")

        #check sign up for confirmation is checked
        checkbox_dec = driver.find_element_by_name("uap")
        AsertTrue(checkbox_dec.is_selected())
        #	fill out	all	the	fields
        first_name.send_keys("Test")
        last_name.send_keys("User1")
        email_adress.send_keys("syzdol.sps105lodz@gmail.com")
        re_type_email.send_keys("syzdol.sps105lodz@gmail.com")
        choose_username.send_keys("tester")
        choose_password.send_keys("tester1")
        re_type_password.send_keys("tester1")
        checkbox_dec.click()

        #	click	Submit	button	to	submit	the	form
