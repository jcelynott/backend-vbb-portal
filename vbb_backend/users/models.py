import enum

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from vbb_backend.utils.models.base import BaseUUIDModel
from vbb_backend.utils.models.question import QuestionareAnswers, QuestionareQuestions


class UserTypeEnum(enum.Enum):
    STUDENT = "100"
    MENTOR = "200"
    ADVISOR = "300"
    DIRECTOR = "400"
    TEACHER = "500"
    HEADMASTER = "600"


UserTypeChoices = [(e.value, e.name) for e in UserTypeEnum]


class User(AbstractUser):
    """Default user for Village Book Builders Backend.
    The AbstractUser Model already includes most of the required fields for a User.
    The Extra fields are used to store details of a user in VBB
    """

    class VerificationLevelEnum(enum.Enum):
        # WE can define what each Level Means and so on or default to VERIFIED
        LEVEL1 = 1
        LEVEL2 = 2
        VERIFIED = 100

    VerificationLevelChoices = [(e.value, e.name) for e in VerificationLevelEnum]

    user_type = models.IntegerField(
        choices=UserTypeChoices, default=UserTypeEnum.MENTOR.value
    )

    verification_level = models.IntegerField(
        choices=VerificationLevelChoices, default=VerificationLevelEnum.LEVEL1.value
    )

    vbb_chapter = models.CharField(
        max_length=40, null=True, blank=True, verbose_name=_("VBB Chapter")
    )
    date_of_birth = ""
    primary_language = models.CharField(max_length=70, null=True, blank=True)
    time_zone = models.CharField(max_length=40, null=True)
    charged = models.TextField(max_length=1024, null=True)  # Mentors Only
    address = models.TextField()  # Mentors Only
    initials = models.CharField(max_length=6, null=True)
    personal_email = models.EmailField(
        null=True, unique=True, verbose_name=_("Personal Email")
    )

    phone = PhoneNumberField(blank=True, verbose_name=_("Phone Number"))
    is_adult = models.BooleanField(default=False)  # Mentors
    occupation = models.CharField(
        max_length=70, null=True, blank=True, verbose_name=_("Occupation")
    )
    affiliation = models.CharField(
        max_length=70, null=True, blank=True, verbose_name=_("Affiliation")
    )  # Mentors Only
    referral_source = models.CharField(
        max_length=200, null=True, blank=True, verbose_name=_("Refferal")
    )
    desired_involvement = models.CharField(
        max_length=200, null=True, blank=True
    )  # Mentors Specific
    city = models.CharField(max_length=70, null=True, blank=True)
    notes = models.TextField(
        max_length=512, null=True, blank=True
    )  # Super User Specific

    def is_verified(self):
        return self.verification_level == self.VerificationLevelEnum.VERIFIED.value


class UserQuestionareQuestions(QuestionareQuestions):
    user_type = models.IntegerField(
        choices=UserTypeChoices, default=None, null=True, blank=True
    )


class UserQuestionareAnswers(QuestionareAnswers):
    question = models.ForeignKey(
        UserQuestionareQuestions,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=False,
        blank=False,
    )


class Student(BaseUUIDModel):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    # Further Student Information Here


class Mentor(BaseUUIDModel):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    # Further Mentor Information Here


class HeadMaster(BaseUUIDModel):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    # Further HeadMaster Information Here
