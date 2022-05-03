from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from .models import UserProfiles


class MyModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ('user',
                    'date_of_birth',
                    # 'sex',
                    # 'preferable_language',
                    'full_name',
                    'main_email')
    raw_id_fields = ['user']


admin.site.register(UserProfiles, MyModelAdmin)
# https://stackoverflow.com/questions/31426010/better-arrayfield-admin-widget
