import enum

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Default user for Village Book Builders Backend."""

    class UserTypeEnum(enum.Enum):
        MENTOR = "0"

    UserTypeChoices = [(e.value, e.name) for e in UserTypeEnum]
    UserType = models.IntegerField(
        choices=UserTypeChoices, default=UserTypeEnum.MENTOR.value
    )


class Mentor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name="mp",
        null=True,
        blank=True,
        verbose_name=_("User Object of Mentor"),
    )
    first_name = models.CharField(
        max_length=254, null=True, verbose_name=_("First Name")
    )
    last_name = models.CharField(max_length=254, null=True, verbose_name=_("Last Name"))
    personal_email = models.EmailField(
        null=True, unique=True, verbose_name=_("Personal Email")
    )
    vbb_email = models.EmailField(
        null=True, unique=True, verbose_name=_("Assigned VBB Email")
    )
    phone = PhoneNumberField(blank=True, verbose_name=_("Phone Number"))
    adult = models.CharField(max_length=3, null=True)
    occupation = models.CharField(
        max_length=70, null=True, blank=True, verbose_name=_("Occupation")
    )
    vbb_chapter = models.CharField(
        max_length=40, null=True, blank=True, verbose_name=_("VBB Chapter")
    )
    affiliation = models.CharField(
        max_length=70, null=True, blank=True, verbose_name=_("Affiliation")
    )
    referral_source = models.CharField(
        max_length=200, null=True, blank=True, verbose_name=_("Refferal")
    )
    languages = models.CharField(max_length=70, null=True, blank=True)
    time_zone = models.CharField(max_length=40, null=True)
    charged = models.TextField(max_length=1024, null=True)
    initials = models.CharField(max_length=6, null=True)
    desired_involvement = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=70, null=True, blank=True)
    advisor_notes = models.TextField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
