# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    fullname = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Ddd(models.Model):

    #__Ddd_FIELDS__
    ddd = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    state_short = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)

    #__Ddd_FIELDS__END

    class Meta:
        verbose_name        = _("Ddd")
        verbose_name_plural = _("Ddd")


class Person(models.Model):

    #__Person_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    ddd = models.ForeignKey(DDD, on_delete=models.CASCADE)

    #__Person_FIELDS__END

    class Meta:
        verbose_name        = _("Person")
        verbose_name_plural = _("Person")


class Company(models.Model):

    #__Company_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    contact = models.ForeignKey(Person, on_delete=models.CASCADE)

    #__Company_FIELDS__END

    class Meta:
        verbose_name        = _("Company")
        verbose_name_plural = _("Company")



#__MODELS__END
