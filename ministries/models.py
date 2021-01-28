from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Ministries(models.Model):
    ministry_heading = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        unique=True)

    sub_title_heading = models.CharField(
        max_length=25,
        null=False,
        blank=False
        )

    bible_verse = models.TextField(max_length=500, null=False, blank=False)
    group_promotion = models.TextField(max_length=500, null=False, blank=False)
    group_leader = models.CharField(max_length=30, null=False, blank=False)
    group_leader_email = models.EmailField(max_length=50, blank=True)

    group_leader_info = models.TextField(
        max_length=350,
        null=False,
        blank=False
        )

    important_information = models.TextField(
        max_length=350,
        null=False,
        blank=False
        )

    def __str__(self):
        return self.ministry_heading


class Message(models.Model):
    ministy = models.ForeignKey(
        Ministries,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, blank=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    message = models.TextField(max_length=100, blank=True)

    street_address1 = models.CharField(
        max_length=80,
        blank=True
        )

    street_address2 = models.CharField(
        max_length=80,
        blank=True
        )

    postcode = models.CharField(
        max_length=20,
        blank=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class WeekDays(models.Model):
    day_name = models.CharField(max_length=30)

    def __str__(self):
        return self.day_name


class MeetingTimes(models.Model):

    meeting_day = models.ForeignKey(
        WeekDays,
        null=True, blank=True,
        on_delete=models.SET_NULL)

    meeting_ministry_name = models.ForeignKey(
        Ministries,
        null=True, blank=True,
        on_delete=models.CASCADE)

    group_lead_by = models.CharField(max_length=25, null=False, blank=False)
    timings = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.group_lead_by
