from django.test import TestCase
from django.urls import reverse

from exchange_point.settings import LOGIN_URL
from django.contrib.auth import get_user_model


class HomePageTest(TestCase):

    def setUp(self):
        self.username = 'john'
        self.password = 'secret123'
        get_user_model().objects.create_user(username=self.username, email='normal@user.com', password=self.password)

    def test_uses_homepage_with_correct_template(self):
        """ Тест: авторизованный пользователь заходит на домашнюю страницу с правильным шаблоном"""
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'layout/base.html')

    def test_redirects_to_login_if_none_authenticated_user(self):
        """ Тест: неавторизованный пользователь направляется на страницу login"""
        response = self.client.get('/')
        self.assertRedirects(response, f'{reverse(LOGIN_URL)}?next=/')
