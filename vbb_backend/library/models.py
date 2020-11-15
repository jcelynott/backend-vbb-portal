import enum
from django.db import models

from vbb_backend.utils.models.base import BaseUUIDModel


class Library(BaseUUIDModel):
    """
    This Model represents a Library in Village Book Builders
    """

    name = models.CharField(max_length=40, null=True, blank=True)
    time_zone = models.CharField(max_length=40, null=True, blank=True)
    calendar_id = models.CharField(max_length=120, null=True)
    whatsapp_group = models.CharField(max_length=60, null=True)
    program_director_name = models.CharField(max_length=50, null=True, blank=True)
    program_director_phone = models.CharField(max_length=15, null=True, blank=True)
    program_director_email = models.EmailField(max_length=50, null=True, blank=True)
    announcements_group = models.CharField(max_length=50, null=True, blank=True)
    collaboration_group = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Libraries"

    def __str__(self):
        return self.name


class LanguageEnum(enum.Enum):
    ENGLISH = "ENGLISH"


LanguageChoices = [(e.value, e.name) for e in LanguageEnum]


class Computer(BaseUUIDModel):
    """
    This Model Represents a Computer in a VBB Library
    """

    library = models.ForeignKey(
        Library,
        on_delete=models.PROTECT,
    )
    language = models.CharField(max_length=254, choices=LanguageChoices)
    computer_number = models.IntegerField(null=True)
    computer_email = models.EmailField(max_length=70, null=True)
    room_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return (
            f"{str(self.library)} {str(self.computer_number)} + ({self.computer_email})"
        )


class Slot(BaseUUIDModel):
    """
    This Model Represents a slot that the library decides to have with one of its computer,
    **eg , a slot can be for a Computer A for firday 10AM to friday 12AM**
    The slot is not editable, once the slot is to be updated the model object has to be deleted and recreated
    The slot object has no starting time or ending time, slots made are run throughout the year, to cancel a slot the slot has to be deleted
    The slot can be of any duration less than 24 hours

    the slot start and end refer to the start and end of a session in the slot,
    we are only concerned with the day of the week and the time , so month and year does not make a difference

    the slot will be assigned to a mentor, which connects the mentor app and the library app

    TODO the language field is conflicted by the language field in the computer , either one has to be removed
    """

    computer = models.ForeignKey(
        Computer,
        on_delete=models.PROTECT,
        related_name="sessionslots",
        null=True,
    )
    language = models.CharField(max_length=254, choices=LanguageChoices)
    start = models.DateTimeField()  # All Date Times in UTC
    end = models.DateTimeField()  # All Date Times are in UTC
    event_id = models.CharField(max_length=60, null=True, blank=True)
    hangouts_link = models.CharField(max_length=60, null=True, blank=True)

    #
    # Assigned Session Variable to be added