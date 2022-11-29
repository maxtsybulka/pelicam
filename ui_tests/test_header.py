"""Поизитивные и негативные тесты хедера"""

import allure
import time
from pages.header import Header
import pytest_check as check


@allure.feature("Хедер")
@allure.story("Проверка элементов хедера")
def test_header(web_browser):
    """ Проверка наличия элементов на экране, контент и функционал хедера. """

    page = Header(web_browser)

    with allure.step("Иконка компании"):
        check.is_true(page.head_leabel.is_presented())
        check.is_true(page.head_leabel.is_visible())
        check.is_true(page.head_leabel.is_clickable())

    with allure.step("Кнопка событий"):
        check.is_true(page.btn_ivent.is_visible())
        check.is_true(page.btn_ivent.is_clickable())
        check.equal(page.btn_ivent.get_text(), 'Wydarzenia')
        check.equal(page.btn_ivent.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка UTM и URL сокращатель"):
        check.is_true(page.btn_utm_url.is_visible())
        check.is_true(page.btn_utm_url.is_clickable())
        check.equal(page.btn_utm_url.get_text(), 'Skracacz UTM i URL')
        check.equal(page.btn_utm_url.get_attribute('href'), 'https://pilicam.com/utm/')

    with allure.step("Кнопка Цены"):
        check.is_true(page.btn_price.is_visible())
        check.is_true(page.btn_price.is_clickable())
        check.equal(page.btn_price.get_text(), 'Cennik')
        check.equal(page.btn_price.get_attribute('href'), 'https://pilicam.com/prices/')

    with allure.step("Кнопка Войти"):
        check.is_true(page.btn_login.is_visible())
        check.is_true(page.btn_login.is_clickable())
        check.equal(page.btn_login.get_text(), 'Zaloguj się')
        check.equal(page.btn_login.get_attribute('href'), 'https://pilicam.com/auth/signin/')

    with allure.step("Кнопка Создать аккаунт"):
        check.is_true(page.btn_create_accaunt.is_visible())
        check.is_true(page.btn_create_accaunt.is_clickable())
        check.equal(page.btn_create_accaunt.get_text(), 'Utwórz konto')
        check.equal(page.btn_create_accaunt.get_attribute('href'), 'https://pilicam.com/auth/signup/')

    with allure.step("Кнопка смены языка"):
        check.is_true(page.btn_leng.is_visible())
        check.is_true(page.btn_leng.is_clickable())
        page.btn_leng.click()

        time.sleep(1)
        # Проверка языка
        check.is_true(page.btn_leng_pl.is_visible())
        check.is_true(page.btn_leng_pl.is_clickable())
        check.equal(page.btn_leng_pl.get_text(), 'PL')

        check.is_true(page.btn_leng_ru.is_visible())
        check.is_true(page.btn_leng_ru.is_clickable())
        check.equal(page.btn_leng_ru.get_text(), 'RU')

        check.is_true(page.btn_leng_en.is_visible())
        check.is_true(page.btn_leng_en.is_clickable())
        check.equal(page.btn_leng_en.get_text(), 'EN')
