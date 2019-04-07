# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=64)

    class Meta:
        table_name = 'user'


class Bill(models.Model):
    amount = models.IntegerField(default=0)
    desc = models.CharField(max_length=255)
    create_time = models.DateField(auto_now_add=True)
    modify_time = models.DateField(auto_now=True)
    user = models.ForeignKey(User, related_name='bills', db_column='user_id')

    class Meta:
        table_name = 'bill'
