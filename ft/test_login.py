import os
import poplib
import re
import time

from django.contrib.auth import get_user_model
from django.core import mail
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

USER_MODEL = get_user_model()

CREDENTIALS = {
    'username': 'john',
    'password': '12345678',
    'email': 'normal@user.com',
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'patronymic': 'Иванович',
}


class LoginTest(FunctionalTest):

    def setUp(self):
        super().setUp()
        self.User = get_user_model()
        self.User.objects.create_user(**CREDENTIALS)
        # Можно еще superuser(). А если просто create(), то (т.к. django хеширует пароль),
        # self.user = self.User.objects.first()
        # self.user.set_password('12345678')
        # self.user.save()

    def test_can_login_logout(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_link_text('Вход').click()

        # Войти под зарегистрированным пользователем
        self.browser.find_element_by_id('username').send_keys(CREDENTIALS['username'])
        # Можно используя скрипт
        self.browser.execute_script(f'document.getElementById("password").value={CREDENTIALS["password"]}')
        self.browser.find_element_by_id('login').click()
        # Проверить наличие имени авторизованного пользователя в соответствующем теге
        self.assertIn(f'{CREDENTIALS["last_name"]} {CREDENTIALS["first_name"]} {CREDENTIALS["patronymic"]}',
                      self.wait_for(
                          lambda: self.browser.find_element_by_class_name('text-light').text
                      ))
        # Выйти
        self.browser.find_element_by_link_text('Выйти').click()
        self.assertIn('Вы успешно вышли',
                      self.wait_for(
                          lambda: self.browser.find_element_by_tag_name('h5').text
                      ))

