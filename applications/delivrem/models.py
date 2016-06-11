# -*- coding: utf-8 -*-
from datetime import timedelta
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator
from django.conf import settings
from basis.models import TimeStampModel
# Create your models here.
'''
 ☐ User
   ☐ **Product (Image)
     ☐ **Comment
     ☐ **Like
     ☐ **Purchase
     ☐ **Repost
'''

class Product(TimeStampModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='delivrem/%Y/%m/%d',
                            help_text='Show us wadiyabi',
                            null=False, blank=False)
    slug = models.CharField(max_length=220, null=True, blank=True)
    showoff = models.CharField(max_length=440, null=True, blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    activated = models.BooleanField(default=False)
    #did this product have been sale
    sale = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Zin(TimeStampModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.CharField(max_length=220, null=False, blank=False)
