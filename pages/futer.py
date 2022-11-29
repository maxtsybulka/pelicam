""" Элементы страницы логирования """

import os
import time

from pages.base_page import WebPage
from pages.elements import WebElement


class Futer(WebPage):
    """ Класс представляющий элементы футер. '"""

    def __init__(self, web_driver, url=""):
        if not url:
            url = (
                    os.getenv("FUTER")
                    or "https://pilicam.com/"
            )

        super().__init__(web_driver, url)

    # Учителя и эксперты
    btn_teacher = WebElement(xpath='//div[@class="landing-blocks-footer"]//a[1]')

    # Онлайн школы
    btn_online_school = WebElement(xpath='//div[@class="landing-blocks-footer"]//a[2]')

    # Школы с оффлайн занятиями
    btn_offline_school = WebElement(xpath='//div[@class="landing-blocks-footer"]//a[3]')

    # Малый бизнес
    btn_small_business = WebElement(xpath='//div[@class="landing-blocks-footer"]//a[4]')

    # Конструктор курсов
    btn_builder = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][2]//a[1]')

    # CRM система
    btn_crm = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][2]//a[2]')

    # Умный календарь
    btn_smart_calendar = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][2]//a[3]')

    # Автоматизация
    btn_automation = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][2]//a[4]')

    # Маркетплейс
    btn_marketplace = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][2]//a[5]')

    # UTM сокращатель
    btn_utm = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][2]//a[6]')

    # Политика конфиденциальности
    btn_privace = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][3]//a[1]')

    # Цены и пакеты
    btn_price = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][3]//a[2]')

    # Договор оферты
    btn_document = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][3]//a[3]')

    # Гарантия PILICAM
    btn_pilicam = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][3]//a[4]')

    # Связаться
    btn_contact = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][4]//a[1]')

    # Внести предложение
    btn_sugastion = WebElement(xpath='//div[@class="landing-blocks-footer"]//div[@class="d-flex flex-column"][4]//a[2]')

    # Facebook
    btn_facebook = WebElement(xpath='//div[@class="mr-4"][1]//a')

    # TikTok
    btn_tiktok = WebElement(xpath='//div[@class="mr-4"][2]//a')

    # Instagram
    btn_instagram = WebElement(xpath='//div[@class="mr-4"][3]//a')

    # Mail
    btn_mail = WebElement(xpath='//div[@class="mr-4"][4]//a')
