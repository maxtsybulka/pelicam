"""Поизитивные и негативные тесты логирования"""

import allure
import time
from pages.login import Login
import pytest_check as check


@allure.feature("Авторизация на сайте")
@allure.story("Проверка входа в профиль")
@allure.severity("BLOCKER")
def test_login(web_browser):
    """ Вход и авторизация на сайте с заполнением корректных данных. """

    page = Login(web_browser)

    with allure.step("Текст политики конф. google"):
        check.is_true(page.text_privacy_policy.is_presented())
        check.is_true(page.text_privacy_policy.is_visible())
        check.equal(page.text_privacy_policy.get_text(), 'Witryna jest chroniona reCAPTCHA, zastosował się'
                                                         ' do niego Polityka prywatności i Warunki Google.')

    with allure.step("Ссылка в тексте 'Политика конфиденциальности'"):
        check.is_true(page.link_privacy_policy.is_visible())
        check.is_true(page.link_privacy_policy.is_clickable())
        check.equal(page.link_privacy_policy.get_attribute('href'), 'https://policies.google.com/privacy')

    with allure.step('Ссылка в тексте "Условия Google"'):
        check.is_true(page.link_google_terms.is_clickable())
        check.is_true(page.link_google_terms.is_clickable())
        check.equal(page.link_google_terms.get_attribute('href'), 'https://policies.google.com/terms')

    with allure.step('Текст "или войти через"'):
        check.is_true(page.text_head_or_login.is_visible())
        check.equal(page.text_head_or_login.get_text(), 'lub zaloguj się przez')

    with allure.step('Кнопка регистрации через google'):
        check.is_true(page.btn_google.is_visible())
        check.is_true(page.btn_google.is_clickable())

    with allure.step('Кнопка регистрации через facebook'):
        check.is_true(page.btn_facebook.is_visible())
        check.is_true(page.btn_facebook.is_clickable())

    with allure.step('Кнопка забыли пароль'):
        check.is_true(page.btn_forgot_pass.is_clickable())
        check.equal(page.btn_forgot_pass.get_attribute('href'), 'https://pilicam.com/auth/passwordreset/')

    with allure.step('Кнопка регистрации'):
        check.is_true(page.btn_register.is_clickable())
        check.equal(page.btn_register.get_attribute('href'), 'https://pilicam.com/auth/signup/')

    with allure.step("Ввод почты"):
        check.is_true(page.input_email.is_visible())
        check.is_true(page.input_email.is_clickable())
        page.input_email.send_keys("maksim.pvo@gmail.com")

    with allure.step("Ввод пароля"):
        check.is_true(page.input_pass.is_visible())
        check.is_true(page.input_pass.is_clickable())
        page.input_pass.send_keys("123456789")

    with allure.step("Кнопка показа пароля"):
        check.is_true(page.btn_show_pass.is_visible())
        check.is_true(page.btn_show_pass.is_clickable())
        page.btn_show_pass.click()

    with allure.step("Кнопка показа пароля"):
        check.is_true(page.btn_login.is_visible())
        check.is_true(page.btn_login.is_clickable())
        page.btn_login.click()
