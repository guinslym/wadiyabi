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
from django.forms.models import model_to_dict
# Create your models here.
'''
 ☐ User
   ☐ **Product (Image)
     ☐ **Comment#
     ☐ **Like
     ☐ **Repost
 ☐ **Follow
'''

class TimeStampedModelMixin(models.Model):
    "Should be mixed in to all models."
    time_created = models.DateTimeField(auto_now_add=True,
                help_text="The time this item was created in the database.")
    time_modified = models.DateTimeField(auto_now=True,
                help_text="The time this item was last saved to the database.")

    class Meta:
        abstract = True



class DiffModelMixin(object):
    """A model mixin that tracks model fields' values and provide some useful
    api to know what fields have been changed.
    eg:
    Get an object from the database.
    Set some of its properties.
    Call `myObj.has_changed` to see if any fields are different to in the DB.
    From http://stackoverflow.com/a/13842223/250962
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial = self._dict

    @property
    def diff(self):
        """Returns a dict of properties that have changed, with values a list
        of before/after changes. eg:
        `{'categories': (None, [1, 3, 5]), 'rank': (0, 42)}`
        """
        d1 = self.__initial
        d2 = self._dict
        diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
        return dict(diffs)

    @property
    def has_changed(self):
        "Returns True if any of the properties have changed."
        return bool(self.diff)

    @property
    def changed_fields(self):
        "Returns a list of property names for any that have changed."
        return self.diff.keys()

    def get_field_diff(self, field_name):
        "Returns a diff for field if it's changed and None otherwise."
        return self.diff.get(field_name, None)

    def save(self, *args, **kwargs):
        "Saves model and set initial state."
        super().save(*args, **kwargs)
        self.__initial = self._dict

    @property
    def _dict(self):
        return model_to_dict(self, fields=[field.name for field in
                             self._meta.fields])



class Product(TimeStampModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='delivrem/%Y/%m/%d',
                            help_text='Show us wadiyabi',
                            null=False, blank=False, verbose_name="pics")
    showoff = models.CharField(max_length=440, null=True, blank=True, verbose_name='shoutout')
    slug = models.CharField(max_length=220, null=True, blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0, null=True, blank=True)
    activated = models.BooleanField(default=False)
    #did this product have been sale
    sale = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Zin(TimeStampModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.CharField(max_length=220, null=False, blank=False)

"""
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

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profiles'
"""
