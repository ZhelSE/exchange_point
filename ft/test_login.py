import os
import poplib
import re
import time
from django.core import mail
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class LoginTest(FunctionalTest):

    def test_can_log_in(self):

        self.browser.get(self.live_server_url)
        self.browser.find_element_by_link_text('Вход').click()

        # Войти под зарегистрированным пользователем
        self.browser.find_element_by_id('username').send_keys('new_user')
        self.browser.find_element_by_id('password').send_keys('12345678')
        self.browser.find_element_by_name('Вход').click()
        # Проверить наличие имени авторизованного пользователя в соответствующем теге
        self.assertIn('new_user',
                      self.wait_for(
                          lambda: self.browser.find_element_by_class_name('text-light').text
                      ))
