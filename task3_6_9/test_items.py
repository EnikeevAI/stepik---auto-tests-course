import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)
    #time.sleep(30)

    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button, "Button add to basket not found"
