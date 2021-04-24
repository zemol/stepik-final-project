from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    
    prod_page.add_product_to_the_basket()
