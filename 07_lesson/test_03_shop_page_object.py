import pytest
from selenium import webdriver
from AutorizationPage import AutorizationPage
from MainPage import MainPage
from CartPage import CartPage
from OrderPage import OrgerPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    autorization_page = AutorizationPage(driver)
    autorization_page.open()
    autorization_page.autorization_login("standard_user")
    autorization_page.autorization_pass("secret_sauce")
    autorization_page.login_button()


    main_page = MainPage(driver)
    main_page.add_product()
    main_page.cart_link()

    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_items()
    expected_items = [
        {'name': 'Sauce Labs Backpack', 'price': '$29.99'},
        {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
        {'name': 'Sauce Labs Onesie', 'price': '$7.99'}
    ]
    assert cart_items == expected_items
    cart_page.checkout()

    order_page = OrgerPage(driver)
    order_page.user_info()
    order_page.making_order()
    total = order_page.total_price()
    assert total == "$58.29"