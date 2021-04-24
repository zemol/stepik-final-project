from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.NAME, "login_submit")

    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocators():
    PROD_ADD = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PROD_NAME = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    PROD_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p strong")
