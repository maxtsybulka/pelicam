""" Элементы страницы логирования """

import os
import time

from pages.base_page import WebPage
from pages.elements import WebElement


class Header(WebPage):
    """Класс представляющий элементы хедера'"""

    def __init__(self, web_driver, url=""):
        if not url:
            url = (
                    os.getenv("HEADER")
                    or "https://pilicam.com/"
            )

        super().__init__(web_driver, url)

    # Иконка компании
    head_leabel = WebElement(xpath='//div[@class="v-toolbar__content"]')

    # Кнопка событий
    btn_ivent = WebElement(xpath='//div[@class="v-toolbar__content"]/a[1]')

    # Кнопка UTM и URL сокращатель
    btn_utm_url = WebElement(xpath='//div[@class="v-toolbar__content"]/a[2]')

    # Кнопка Цены
    btn_price = WebElement(xpath='//div[@class="v-toolbar__content"]/a[3]')

    # Кнопка Войти
    btn_login = WebElement(xpath='//div[@class="v-toolbar__content"]/a[4]')

    # Кнопка Создать аккаунт
    btn_create_accaunt = WebElement(xpath='//div[@class="v-toolbar__content"]/a[5]')

    # Кнопка смены языка
    btn_leng = WebElement(xpath='//button[@type="button"]')

    # Кнопка смены языка PL
    btn_leng_pl = WebElement(xpath='//div[@class="v-list v-sheet theme--light"]//div[@tabindex="0"][1]')

    # Кнопка смены языка RU
    btn_leng_ru = WebElement(xpath='//div[@class="v-list v-sheet theme--light"]//div[@tabindex="0"][2]')

    # Кнопка смены языка EN
    btn_leng_en = WebElement(xpath='//div[@class="v-list v-sheet theme--light"]//div[@tabindex="0"][3]')
