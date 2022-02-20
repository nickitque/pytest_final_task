import time
import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_open_product_page(browser):
    page = MainPage(browser, link)
    page.open()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_messages()


def test_find_basket_button(browser):
    browser.get(url)
    basket_button = browser.find_elements_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
    """The examiner has himself add time.sleep"""
    assert basket_button, "There is no element of basket button"


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_products_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_messages()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Открываем страницу товара. Добавляем товар в корзину. Проверяем,
    что нет сообщения об успехе с помощью is_not_element_present"""
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """Открываем страницу товара. Проверяем, что нет сообщения об успехе
    с помощью is_not_element_present"""
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    """Открываем страницу товара, Добавляем товар в корзину.
    Проверяем, что нет сообщения об успехе с помощью is_disappeared"""
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.is_element_dissapeared()