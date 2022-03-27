from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()

    def matem(self):
        self.solve_quiz_and_get_code()

    def added_product_in_basket(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        assert name_book in product_in_basket, "Нет сообщения о том, что товар добавлен в корзину"

    def name_book_in_message(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        message_name_book = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_BOOK).text
        assert name_book == message_name_book, "Название книги не совпадает"

    def price_book_in_message(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        message_price_book = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BOOK).text
        assert price_book == message_price_book, "Стоимость книги не совпадает"