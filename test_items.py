import time

class TestButtonAddToBasket():

	def test_button_add_to_basket(self, browser):
		browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
		#time.sleep(6)
		button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
		assert len(button) == 1, "No button for add to basket or class isn't unique"