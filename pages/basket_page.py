from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def nothing_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), 'В корзине есть товар (товары)'
        assert self.is_element_present(*BasketPageLocators.NOTHING_IN_BASKET), 'В корзине есть товар!'
