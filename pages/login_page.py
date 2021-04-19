from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Emial field on the login page is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Password field on the login page is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Submit button on the login page is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Emial field on the register page is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS1), "Password field on the register page is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS2), "Repeat password field on the register page is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_SUBMIT), "Submit button on the register page is not presented"
