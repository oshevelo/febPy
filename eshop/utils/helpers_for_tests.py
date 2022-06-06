import json
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


def create_user(username, superuser=False, user_kwargs_dict=None):
    user_kwargs_dict = user_kwargs_dict or dict()

    set_staff = False

    if superuser:
        set_staff = True

    user_kw = dict(
        username=username,
        password='111',
        email=username + '@email.com',
        is_active=True,
        is_staff=set_staff,
        is_superuser=superuser
    )

    user_kw.update(user_kwargs_dict)
    user_kw['password'] = make_password(user_kw['password'])
    user = User.objects.create(**user_kw)

    return user
