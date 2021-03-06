from django.contrib.auth.models import AbstractUser
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username_validator = None
    username = None
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(_('Email Address'), unique=True)
    balance = models.FloatField(_('Balance'), default=0)
    objects = UserManager()

    def __str__(self):
        return 'User [{}]'.format(self.email)

    @transaction.atomic
    def update_balance(self, balance_change):
        self.balance += balance_change
        self.save()
