from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AppsUser


class AppsUserAdmin(UserAdmin):
    save_on_top = True
    list_display = ['username', 'get_fio', 'domain_account']
    list_display_links = ['username', 'get_fio', ]
    fieldsets = (
        (None,
         {'fields': ('username', 'password')}),
        ('Персональная информация',
         {'fields': ('last_name', 'first_name', 'patronymic', 'email',
                     'domain_account', 'position', 'location')}),
        ('Права доступа',
         {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                     'user_permissions')}),
        ('Важные даты',
         {'fields': ('last_login', 'date_joined')})
    )

    def get_fio(self, obj):
        return f'{obj.last_name} {obj.first_name} {obj.patronymic}'

    get_fio.short_description = 'ФИО'


admin.site.register(AppsUser, AppsUserAdmin)
