from selenium import webdriver

from selenium.webdriver.common.keys import Keys

# redirection to sps105.szkolnastrona.pl
driver = webdriver.Chrome()
driver.get("http://zss3.szkolnastrona.pl/")
driver.close()


# get the	search	textbox
def test_search_element_name(self):
    self.search_field = self.driver.find_element_by_name("kword")


# check lenght
def test_search_text_max_lenght(self):
    self.assertEqual(40, search_field.get_attribute("maxlength"))


def test_search_button_enabled(self):
    #	get	Search	button
    search_button = self.driver.find_element_by_class_name("search")
    #	check	Search	button	is	enabled
    self.assertTrue(search_button.is_enable)


# get button
def test_search_element(self):
    self.search_element = self.driver.find_element_by_id("search-input")
