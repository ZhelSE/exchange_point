from django.test import TestCase
from django.urls import reverse

from exchange_point.settings import LOGIN_URL
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

CREDENTIALS = {
    'username': 'john',
    'password': '12345678',
    'email': 'normal@user.com',
}


class HomePageTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(**CREDENTIALS)

    def test_uses_homepage_with_correct_template(self):
        """ Тест: авторизованный пользователь заходит на домашнюю страницу с правильным шаблоном"""
        self.client.login(**CREDENTIALS)
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'layout/base.html')

    def test_redirects_to_login_if_none_authenticated_user(self):
        """ Тест: неавторизованный пользователь направляется на страницу login"""
        response = self.client.get('/')
        self.assertRedirects(response, f'{reverse(LOGIN_URL)}?next=/')
