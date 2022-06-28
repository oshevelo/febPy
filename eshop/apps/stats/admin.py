from django.contrib import admin

from .models import UserAction


class UserActionAdmin(admin.ModelAdmin):

    fields = ['user', 'data']

admin.site.register(UserAction, UserActionAdmin)
