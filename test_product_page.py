from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('end', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])


def test_guest_can_add_product_to_basket(browser, end):
    browser.delete_all_cookies()
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{end}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.matem()
    page.added_product_in_basket()
    page.name_book_in_message()
    page.price_book_in_message()
