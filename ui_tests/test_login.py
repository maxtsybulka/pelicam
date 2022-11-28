"""Поизитивные и негативные тесты логирования"""

import allure
import time
from pages.login import Login


@allure.feature("Авторизация на сайте")
@allure.story("Проверка входа в профиль")
@allure.severity("BLOCKER")
def test_login(web_browser):
    """ Вход и авторизация на сайте с заполнением корректных данных. """

    page = Login(web_browser)

    with allure.step("Ввод почты"):
        page.input_email.send_keys("maksim.pvo@gmail.com")

    with allure.step("Ввод пароля"):
        page.input_pass.send_keys("1qaz@WSX")

    with allure.step("Показ пароля"):
        page.btn_show_pass.click()

    with allure.step("Вход в кабинет"):
        page.btn_login.click()
        time.sleep(8)

    with allure.step("Результаты входа в профиль"):
        assert (
            page.name_user.get_text() == "maksim.tsibulko@hoster.by"
        ), f"Вход в профиль {page.name_user.get_text()} не произошел"
