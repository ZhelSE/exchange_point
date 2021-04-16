from django.contrib.auth.models import AbstractUser
from django.db import models


class AppsUser(AbstractUser):
    domain_account = models.CharField(max_length=50, blank=True, verbose_name='Учетная запись')
    patronymic = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    position = models.CharField(max_length=50, blank=True, verbose_name='Должность')
    location = models.CharField(max_length=50, blank=True, verbose_name='Кабинет')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def full_representation(self):
        return f'{self.position} {self.__str__()}'
