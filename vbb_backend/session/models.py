from django.db import models

from vbb_backend.utils.models.base import BaseUUIDModel

from vbb_backend.program.models import Slot

from vbb_backend.users.models import User


class SessionRule(BaseUUIDModel):
    """
    This Model represents the start of a Session which can go on indefenitely or be deleted at some point
    The Session Rule will be tied to a Library Computer Slot
    """

    slot = models.ForeignKey(
        Slot, on_delete=models.SET_NULL, null=True
    )  # Represents the Connected Slot
    start = models.DateTimeField()  # All Date Times in UTC
    end = models.DateTimeField(null=True, blank=True)  # All Date Times in UTC
    mentor = models.ForeignKey(User, on_delete=models.PROTECT)


class Session(BaseUUIDModel):
    """
    This Model represents the sessions history and the next upcoming session for mentors.
    An Asyncronous task will populate the required sessions from the SessionRule
    """

    derived_from = models.ForeignKey(SessionRule, on_delete=models.PROTECT)
    notes = models.TextField(default=None, null=True, blank=True)
    start = models.DateTimeField()  # All Date Times in UTC
    end = models.DateTimeField()  # All Date Times in UTC
    is_mentor_confirmed = models.BooleanField(default=None)
    # TODO: do we no longer need an "is_student_confirmed" field?


class StudentSessionAssociation(BaseUUIDModel):
    """
    This connects the student user object with a Slot Object
    """

    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True)
    wont_attend = models.BooleanField(default=None, null=True)
    is_absent = models.BooleanField(default=None, null=True)
    notes = models.TextField(default=None, null=True)
