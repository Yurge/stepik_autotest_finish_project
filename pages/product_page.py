from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()


    def matem(self):
        self.solve_quiz_and_get_code()


    def should_be_success_message(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        product_in_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert name_book in product_in_basket, "Нет сообщения об успешном добавлении товара в корзину"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение об успешном добавлении товара в корзину есть, но его не должно быть"


    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение об успешном добавлении товара в корзину должно исчезать, но оно не исчезло"


    def name_book_in_message(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        message_name_book = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_BOOK).text
        assert name_book == message_name_book, "Название книги не совпадает"


    def price_book_in_message(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        message_price_book = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BOOK).text
        assert price_book == message_price_book, "Стоимость книги не совпадает"