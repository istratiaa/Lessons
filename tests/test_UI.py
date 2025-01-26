from lesson_playwright.checkout_page import CheckoutPage
from lesson_playwright.inventory_page import InventoryPage
from lesson_playwright.login_page import LoginPage


def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_card()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('John', 'Doe', "12535")
    checkout_page.start_continue()
    inventory_page.logout()