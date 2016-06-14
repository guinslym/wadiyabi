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
import datetime
from django.utils import timezone
# Create your models here.
'''
 ☐ User
   ☐ **Product (Image)
     ☐ **Comment#
     ☐ **Like
     ☐ **Repost
 ☐ **Follow
'''

class Product(TimeStampModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='delivrem/%Y/%m/%d',
                            help_text='Show us wadiyabi',
                            null=False, blank=False)
    slug = models.CharField(max_length=220, null=True, blank=True)
    showoff = models.CharField(max_length=440, null=True, blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0, null=True, blank=True)
    activated = models.BooleanField(default=False)
    #did this product have been sale
    sale = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Zin(TimeStampModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.CharField(max_length=220, null=False, blank=False)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    genderChoice = ( ('M','Male') , ('F','Female')) # adding choicefield for gender
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(auto_now=True)
    profilePic = models.FileField(upload_to='profile/',default='profile/egg.jpg',null=True)
    gender=models.CharField(max_length=10,choices=genderChoice)
    homeTown=models.CharField(max_length=50,blank=True)
    currentPlace=models.CharField(max_length=50,blank=True)
    lastUpdated=models.DateField(auto_now=True)

    '''
    def __str__(self):
        return self.user.username
    '''

    class Meta:
        verbose_name_plural=u'User profiles'
