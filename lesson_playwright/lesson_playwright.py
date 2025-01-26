from playwright.sync_api import sync_playwright
import time
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=500)
page = browser.new_page()
page.goto("http://www.saucedemo.com/")
page.type(selector="#user-name", text="standard_user", delay=100)
page.fill(selector="#password", value="secret_sauce")
page.click(selector=".submit-button")    # [class= "submit-button"]

page.wait_for_url("https://www.saucedemo.com/inventory.html", timeout=10000)
page.wait_for_selector('#inventory_container')

button_add_card = '[data-test="add-to-cart-sauce-labs-backpack"]'
alt_locator_for_button = '.inventory_item a:has-text("Sauce Labs Backpack")'
card_button = '.inventory_item_description:has-text("Sauce Labs Backpack") button:has-text("Add to cart")'

page.is_visible(selector=button_add_card)
page.is_enabled(selector=button_add_card)
# page.click(selector=button_add_card)
# page.click(selector=alt_locator_for_button)
page.click(card_button)
page.is_visible('[data-test="shopping-cart-link"]')
page.click('[data-test="shopping-cart-link"]')
page.wait_for_url("https://www.saucedemo.com/cart.html", timeout=10000)

button_checkout = '#checkout'
page.wait_for_selector(button_checkout)
page.is_visible(button_checkout)
page.is_enabled(button_checkout)
page.click(button_checkout)
page.wait_for_url('https://www.saucedemo.com/checkout-step-one.html')

time.sleep(2)

browser.close()
playwright.stop()