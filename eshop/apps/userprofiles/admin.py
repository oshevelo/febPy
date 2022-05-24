from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
# https://stackoverflow.com/questions/31426010/better-arrayfield-admin-widget
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ('user',
                    'date_of_birth',
                    # 'sex',
                    # 'preferable_language',
                    'full_name',
                    'main_email')
    raw_id_fields = ['user']


admin.site.register(UserProfile, UserProfileAdmin)

