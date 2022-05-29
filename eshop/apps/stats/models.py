from django.db import models
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone

# user - инфо для аутентификации
# user_profile Профиль это разширение для человека то еcть разширенное описание человека,
# предпочтения раpython manage.py migrateзные из товаров магазина, лог предыдущих покупок
# user_account -  это личный счет для бонусов
# модель может иметь одно или больше полей. Каждое поле соответствует полю в таблице. make migration and then migrate
# python manage.py migrate git commit -m ""

# python manage.py makemigrations polls после завершения создания моделей

class UserAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    data = models.JSONField()
    pub_date = models.DateTimeField("date action")

    #anon = User.get_anonymous()

    # считаем кол-во походов на сайт

    def count_entrance_user(self, entrance_counter=0, user=user):
        if user:
            return entrance_counter + 1




