from django.db import models
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# user - инфо для аутентификации
# user_profile Профиль это разширение для человека то еcть разширенное описание человека,
# предпочтения разные из товаров магазина, лог предыдущих покупок
# user_account -  это личный счет для бонусов
# модель может иметь одно или больше полей. Каждое поле соответствует полю в таблице.


class UserAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    data = models.JSONField()
    pub_date = models.DateTimeField("date action", auto_now_add=True)

    #anon = User.get_anonymous()

    # считаем кол-во походов на сайт

    def count_entrance_user(self, user=user):
        return UserAction.object.filter(data__action='login', user=user).count()




