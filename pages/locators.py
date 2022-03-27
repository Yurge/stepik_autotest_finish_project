from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")


class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alertinner")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_BOOK = (By.CSS_SELECTOR, "p.price_color")
    MESSAGE_NAME_BOOK = (By.CSS_SELECTOR, ".alertinner strong")
    MESSAGE_PRICE_BOOK = (By.CSS_SELECTOR, ".alertinner p strong")