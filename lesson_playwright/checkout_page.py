from lesson_playwright.base_page import BasePage


class CheckoutPage(BasePage):
    BUTTON_CHECKOUT_SELECTOR = '#checkout'
    FIRST_NAME_SELECTOR = '#first-name'
    LAST_NAME_SELECTOR = '#last-name'
    POSTAL_CODE_SELECTOR = 'input[name="postalCode"]'
    BUTTON_CONTINUE_SELECTOR = '[data-test="continue"]'
    BUTTON_FINISH_SELECTOR = '[data-test="finish"]'
    BUTTON_BACK_HOME_SELECTOR = '[data-test="back-to-products"]'


    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-one.html'

    def start_checkout(self):
        self.wait_for_selector_and_click(self.BUTTON_CHECKOUT_SELECTOR)
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)
        self.assert_text_present_on_page('Checkout: Your Information')

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait_for_selector_and_type(self.FIRST_NAME_SELECTOR, first_name, 100)
        self.wait_for_selector_and_type(self.LAST_NAME_SELECTOR, last_name, 100)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code, 100)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)

    def start_continue(self):
        self.wait_for_selector_and_click(self.BUTTON_CONTINUE_SELECTOR)
        self.assert_text_present_on_page('Checkout: Overview')
        self.wait_for_selector_and_click(self.BUTTON_FINISH_SELECTOR)
        self.assert_text_present_on_page('Checkout: Complete!')
        self.wait_for_selector_and_click(self.BUTTON_BACK_HOME_SELECTOR)

