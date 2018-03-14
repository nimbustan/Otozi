# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    """
    Bu model kullanıcılar için kullanılacaktır.
    """

    adres = models.CharField(max_length=255, null=True, blank=True)
    telefon = models.CharField(max_length=255, null=True, blank=True)
    biografi = models.TextField()
    github = models.URLField()
    linkedin = models.URLField()
    resim = models.ImageField(upload_to='KullaniciResimleri/%Y/%m/%d', default='KullaniciResimleri/resim.png')