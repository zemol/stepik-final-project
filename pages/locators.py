from selenium.webdriver.common.by import By

class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    pass

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
    BASKET_NAME = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p strong")
    PROD_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PROD_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
