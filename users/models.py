
from django.db import models
from django.contrib.auth.models import User


class ConfirmUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True
                                )
    date = models.DateField(auto_now_add=True, verbose_name='Время создания')
    code = models.CharField(max_length=6)

    def __str__(self):
        return str(self.user)

    @property
    def get_code(self):
        return self.code
