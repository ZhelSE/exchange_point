from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.username = 'john'
        cls.password = 'secret123'
        cls.User.objects.create(username=cls.username,
                                password=cls.password,
                                email='normal@user.com',
                                first_name='Иван',
                                last_name='Иванов',
                                domain_account='Учетная запись',
                                patronymic='Иванович',
                                position='Должность',
                                location='Кабинет № 4',
                                )
        cls.user = cls.User.objects.first()

    def test_correct_str(self):
        self.assertEqual(self.user.__str__(), 'Иванов Иван Иванович')

    def test_correct_full_representation(self):
        self.assertEqual(self.user.full_representation(), 'Должность Иванов Иван Иванович')
