from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):

#    def go_to_login_page(self):
#        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#        login_link.click()
#        #return LoginPage(browser = self.browser, url = self.browser.current_url)
#        alert = self.browser.switch_to.alert
#        allert.accept()
#
#    def should_be_login_link(self):
#        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
