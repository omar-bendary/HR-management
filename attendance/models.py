from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    DAYS = (
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THR', 'Thursday'),
        ('FRI', 'Friday'),
    )
    employee_username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="employees")
    name = models.CharField(max_length=255)
    day = models.CharField(max_length=3, choices=DAYS)
    check_in = models.DateTimeField(auto_now_add=True, help_text="Check-in")
    check_out = models.DateTimeField(help_text="Check-out")

    def save(self, *args, **kwargs):
        self.check_in = timezone.localtime()
        super(Record, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
