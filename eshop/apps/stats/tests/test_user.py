from django.contrib.auth.hashers import make_password

user_kw = dict(
            username='admin',
            password='111',
            email='admin' + '@gmail.com',
        )

user_kw['password'] = make_password(user_kw['password'])
