from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from datetime import date


class User(AbstractUser):
    name = models.CharField(_("Full Name"), blank=True, max_length=255)

    birthday = models.DateField(_('Birthday'),null=True, blank=True)

    MEMBERSHIP_STATUS_CHOICES = (
        ('0', 'Free'),
        ('1', 'Premium'),
        ('2', 'Enterprise'),
    )
    membership_status = models.CharField(
        _('Membership'),
        max_length=1,
        choices=MEMBERSHIP_STATUS_CHOICES,
        default='0'
    )

    def __str__(self):
        if self.birthday:
            born = self.birthday
            today = date.today()
            return "I'm {}, I'm {} years old.".format(
                self.name,
                today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            )
        return "Hi, I'm {}.".format(self.name)

    def get_membership_int(self):
        '''convert str into int, thus making it easier to compare'''
        return int(self.membership_status)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
