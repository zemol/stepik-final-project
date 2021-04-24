import time
from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_the_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.PROD_ADD)
        add_button.click()

        self.solve_quize_and_get_code()

        self.should_be_same_product_in_the_basket()
        self.should_be_same_price_in_the_basket()

    def should_be_same_product_in_the_basket(self):
        #time.sleep(30)
        name = self.browser.find_element(*ProductPageLocators.PROD_NAME)
        basket_name = name
        assert name == basket_name, "Name of the product is not equal to the name in the basket"

    def should_be_same_price_in_the_basket(self):
        #time.sleep(30)
        price = self.browser.find_element(*ProductPageLocators.PROD_PRICE)
        basket_price = price
        assert price == basket_price, "Price of the product is not equal to the price in the basket"
