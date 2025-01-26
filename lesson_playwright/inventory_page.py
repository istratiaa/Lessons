from lesson_playwright.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CARD_SELECTOR = '.inventory_item_description:has-text("Sauce Labs Backpack") button:has-text("Add to cart")'
    SHOPPING_CART_LINK_SELECTOR = '[data-test="shopping-cart-link"]'
    BUTTON_MENU = '#react-burger-menu-btn'
    BUTTON_LOGOUT = '#logout_sidebar_link'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/inventory.html'

    def add_first_item_to_card(self):
        self.wait_for_selector_and_click(self.ADD_TO_CARD_SELECTOR)
        self.assert_element_is_visible(self.SHOPPING_CART_LINK_SELECTOR)
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)

    def logout(self):
        self.assert_text_present_on_page('Products')
        self.wait_for_selector_and_click(self.BUTTON_MENU)
        self.wait_for_selector_and_click(self.BUTTON_LOGOUT)
        self.page.wait_for_url("https://www.saucedemo.com/")