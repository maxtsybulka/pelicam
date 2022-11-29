"""Поизитивные и негативные тесты футера"""

import allure
from pages.futer import Futer
import pytest_check as check


@allure.feature("Футер")
@allure.story("Проверка элементов футера")
def test_futer(web_browser):
    """ Проверка наличия элементов на экране, контент и функционал футера. """

    page = Futer(web_browser)

    with allure.step("Кнопка Учителя и эксперты"):
        check.is_true(page.btn_teacher.is_visible())
        check.is_true(page.btn_teacher.is_clickable())
        check.equal(page.btn_teacher.get_text(), 'Nauczyciele i eksperci')
        check.equal(page.btn_teacher.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Онлайн школы"):
        check.is_true(page.btn_online_school.is_visible())
        check.is_true(page.btn_online_school.is_clickable())
        check.equal(page.btn_online_school.get_text(), 'Szko.ły online')
        check.equal(page.btn_online_school.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Школы с оффлайн занятиями"):
        check.is_true(page.btn_offline_school.is_visible())
        check.is_true(page.btn_offline_school.is_clickable())
        check.equal(page.btn_offline_school.get_text(), 'Szkoły z zajęciami offline')
        check.equal(page.btn_offline_school.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Малый бизнес"):
        check.is_true(page.btn_small_business.is_visible())
        check.is_true(page.btn_small_business.is_clickable())
        check.equal(page.btn_small_business.get_text(), 'Mały biznes')
        check.equal(page.btn_small_business.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Конструктор курсов"):
        check.is_true(page.btn_builder.is_visible())
        check.is_true(page.btn_builder.is_clickable())
        check.equal(page.btn_builder.get_text(), 'Kreator kursów')
        check.equal(page.btn_builder.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка CRM система"):
        check.is_true(page.btn_crm.is_visible())
        check.is_true(page.btn_crm.is_clickable())
        check.equal(page.btn_crm.get_text(), 'System CRM')
        check.equal(page.btn_crm.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Умный календарь"):
        check.is_true(page.btn_smart_calendar.is_visible())
        check.is_true(page.btn_smart_calendar.is_clickable())
        check.equal(page.btn_smart_calendar.get_text(), 'Inteligentny kalendarz')
        check.equal(page.btn_smart_calendar.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Автоматизация"):
        check.is_true(page.btn_automation.is_visible())
        check.is_true(page.btn_automation.is_clickable())
        check.equal(page.btn_automation.get_text(), 'Automatyzacja')
        check.equal(page.btn_automation.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Маркетплейс"):
        check.is_true(page.btn_marketplace.is_visible())
        check.is_true(page.btn_marketplace.is_clickable())
        check.equal(page.btn_marketplace.get_text(), 'Rynek')
        check.equal(page.btn_marketplace.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка UTM сокращатель"):
        check.is_true(page.btn_utm.is_visible())
        check.is_true(page.btn_utm.is_clickable())
        check.equal(page.btn_utm.get_text(), 'Skracacz UTM')
        check.equal(page.btn_utm.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Политика конфиденциальности"):
        check.is_true(page.btn_privace.is_visible())
        check.is_true(page.btn_privace.is_clickable())
        check.equal(page.btn_privace.get_text(), 'Polityka prywatności')
        check.equal(page.btn_privace.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Цены и пакеты"):
        check.is_true(page.btn_price.is_visible())
        check.is_true(page.btn_price.is_clickable())
        check.equal(page.btn_price.get_text(), 'Ceny i pakiety')
        check.equal(page.btn_price.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Договор оферты"):
        check.is_true(page.btn_document.is_visible())
        check.is_true(page.btn_document.is_clickable())
        check.equal(page.btn_document.get_text(), 'Oferta umowya')
        check.equal(page.btn_document.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Гарантия PILICAM"):
        check.is_true(page.btn_pilicam.is_visible())
        check.is_true(page.btn_pilicam.is_clickable())
        check.equal(page.btn_pilicam.get_text(), 'Gwarancja PILICAM')
        check.equal(page.btn_pilicam.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Связаться"):
        check.is_true(page.btn_contact.is_visible())
        check.is_true(page.btn_contact.is_clickable())
        check.equal(page.btn_contact.get_text(), 'Kontakt')
        check.equal(page.btn_contact.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Внести предложение"):
        check.is_true(page.btn_sugastion.is_visible())
        check.is_true(page.btn_sugastion.is_clickable())
        check.equal(page.btn_sugastion.get_text(), 'Zasugerować')
        check.equal(page.btn_sugastion.get_attribute('href'), 'https://pilicam.com/')

    with allure.step("Кнопка Facebook"):
        check.is_true(page.btn_facebook.is_visible())
        check.is_true(page.btn_facebook.is_clickable())
        check.equal(page.btn_facebook.get_attribute('href'), 'https://www.facebook.com/profile.php?id=100063628714118')

    with allure.step("Кнопка TikTok"):
        check.is_true(page.btn_tiktok.is_visible())
        check.is_true(page.btn_tiktok.is_clickable())
        check.equal(page.btn_tiktok.get_attribute('href'), 'https://www.tiktok.com/@pilicamadmin')

    with allure.step("Кнопка Instagram"):
        check.is_true(page.btn_instagram.is_visible())
        check.is_true(page.btn_instagram.is_clickable())
        check.equal(page.btn_instagram.get_attribute('href'), 'https://www.instagram.com/pilicam_com')

    with allure.step("Кнопка Mail"):
        check.is_true(page.btn_mail.is_visible())
        check.is_true(page.btn_mail.is_clickable())
        check.equal(page.btn_mail.get_attribute('href'), 'mailto:contact@pilicam.com')
