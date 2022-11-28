""" Элементы страницы логирования """

import os
import time

from pages.base_page import WebPage
from pages.elements import WebElement


class Login(WebPage):
    """Класс представляющий страницу логирования"""

    def __init__(self, web_driver, url=""):
        if not url:
            url = (
                    os.getenv("LOGIN")
                    or "https://pilicam.com/auth/signin/"
            )

        super().__init__(web_driver, url)

    # Заглавный текст
    text_head = WebElement(xpath='//div[@class="v-card__title text-h1 font-weight-medium text-center color-purple--text justify-center mb-2"]')

    # Подтекст заглавный
    text_head_description = WebElement(xpath='//div[@class="v-card__subtitle text-body-2 text-center mb-4"]')

    # Инпут почты
    input_email = WebElement(xpath='//input[@name="login"]')

    # Инпут пароля
    input_pass = WebElement(xpath='//input[@name="password"]')

    # Кнопка показа пароля
    btn_show_pass = WebElement(xpath='//div[@class="v-card__text pa-0"]//button[@type="button"]')

    # Кнопка входа в аккаунт
    btn_login = WebElement(xpath='//div[@class="v-card__text pa-0"]//button[@id="recaptcha-container"]')

    # Текст политики конф. google
    text_privacy_policy = WebElement(xpath='//div[@class="v-card__text pa-0"]//div[@class="text-h4 text-center mt-1 mb-4 px-2"]')

    # Ссылка в тексте "Политика конфиденциальности"
    link_privacy_policy = WebElement(xpath='//div[@class="v-card__text pa-0"]//div[@class="text-h4 text-center mt-1 mb-4 px-2"]/a[1]')

    # Ссылка в тексте "Условия Google"
    link_google_terms = WebElement(xpath='//div[@class="v-card__text pa-0"]//div[@class="text-h4 text-center mt-1 mb-4 px-2"]/a[2]')

    # Текст "или войти через"
    text_head_or_login = WebElement(xpath='//div[@class="v-card__text pa-0"]//div[@class="d-flex align-center mb-4"]//div[@class="text-h3 mx-2"]')

    # Кнопка регистрации через google
    btn_google = WebElement(css_selector='#app > div.v-application--wrap > main > div > div > div.v-card__actions.pa-0.mb-4 > button:nth-child(1)')

    # Кнопка регистрации через facebook
    btn_facebook = WebElement(css_selector='#app > div.v-application--wrap > main > div > div > div.v-card__actions.pa-0.mb-4 > button:nth-child(3)')

    # Кнопка забыли пароль
    btn_forgot_pass = WebElement(css_selector='#app > div.v-application--wrap > main > div > div > div.v-card__actions.pa-0.justify-space-between > div > a:nth-child(1) > button')

    # Кнопка регистрации
    btn_register = WebElement(css_selector='#app > div.v-application--wrap > main > div > div > div.v-card__actions.pa-0.justify-space-between > div > a:nth-child(2) > button')