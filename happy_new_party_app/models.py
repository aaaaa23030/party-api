from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    content = models.CharField(max_length=1000)
    photo = models.ImageField()
    type_choices = [
        ('пасив', 'Пасив'),
        ('актив', 'Актив'),
    ]
    type = models.CharField(max_length=10, choices=type_choices)
    alcohol = models.BooleanField(default=False)
    age_restrictions_choices = [
        ('<18', 'Меньше 18'),
        ('>18', 'Больше 18'),
    ]
    age_restrictions = models.CharField(max_length=3, choices=age_restrictions_choices)
    gender_choices = [
        ('мужчина', 'Мужчина'),
        ('женщина', 'Женщина'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    members = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.title