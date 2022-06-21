import json
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


def create_user(username, user_kwargs_dict=None):
    user_kwargs_dict = user_kwargs_dict or dict()

    user_kw = dict(
        username=username,
        password='111',
        email=username + '@email.com',
        is_active=True,
    )

    user_kw.update(user_kwargs_dict)
    user_kw['password'] = make_password(user_kw['password'])
    user = User.objects.create(**user_kw)

    return user


def create_superuser(username, user_kwargs_dict=None):
    user_kwargs_dict = user_kwargs_dict or dict()

    user_kw = dict(
        username=username,
        password='111',
        email=username + '@email.com',
        is_active=True,
        is_staff=True,
        is_superuser=True
    )

    user_kw.update(user_kwargs_dict)
    user_kw['password'] = make_password(user_kw['password'])
    user = User.objects.create(**user_kw)

    return user
