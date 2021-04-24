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
        basket_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME)
        name = self.browser.find_element(*ProductPageLocators.PROD_NAME)
        assert name.text == basket_name.text, "Name of the product is not equal to the name in the basket"

    def should_be_same_price_in_the_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PROD_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert price.text == basket_price.text, "Price of the product is not equal to the price in the basket"
