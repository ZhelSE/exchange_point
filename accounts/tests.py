from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from exchange_point.settings import LOGOUT_URL, LOGIN_URL, LOGIN_REDIRECT_URL


class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_model = get_user_model()
        cls.credentials = {
            'username': 'john',
            'password': '12345678',
            'email': 'normal@user.com',
            'first_name': 'Иван',
            'last_name': 'Иванов',
            'patronymic': 'Иванович',
            'position': 'Должность',
        }
        cls.user_model.objects.create_user(**cls.credentials)
        cls.login_url = reverse(LOGIN_URL)
        cls.login_redirect_url = reverse(LOGIN_REDIRECT_URL)
        cls.login_template = 'registration/login.html'
        cls.login_view = 'LoginView'
        cls.logout_url = reverse(LOGOUT_URL)
        cls.logout_template = 'registration/logout.html'
        cls.logout_view = 'LogoutView'


class UserModelTest(UserTest):

    @classmethod
    def setUpTestData(cls):
        super(UserModelTest, cls).setUpTestData()
        cls.user = cls.user_model.objects.first()

    def test_correct_str(self):
        self.assertEqual(self.user.__str__(), 'Иванов Иван Иванович')

    def test_correct_full_representation(self):
        self.assertEqual(self.user.full_representation(), 'Должность Иванов Иван Иванович')


class LogInTest(UserTest):

    def test_login_with_correct_credentials(self):
        response = self.client.post(self.login_url, self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_correct_redirect(self):
        response = self.client.post(self.login_url, self.credentials, follow=True)
        self.assertRedirects(response, self.login_redirect_url)

    def test_login_used_correct_view(self):
        self.assertIn(self.login_view, str(resolve(self.login_url).func.view_class))

    def test_login_used_correct_template(self):
        response = self.client.post(self.login_url, )
        self.assertTemplateUsed(response, self.login_template)


class LogOutTest(UserTest):

    def test_logout_user(self):
        response = self.client.post(self.logout_url, )
        self.assertFalse(response.context['user'].is_authenticated)

    def test_logout_used_correct_view(self):
        self.assertIn(self.logout_view, str(resolve(self.logout_url).func.view_class))

    def test_logout_used_correct_template(self):
        response = self.client.post(self.logout_url, )
        self.assertTemplateUsed(response, self.logout_template)
