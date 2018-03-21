import random
import string
from django.db import models
from django.core.validators import RegexValidator


def generate_key(length=20):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


# TODO: Make date of birth interactive
# TODO: Make Ticket Generation for each complaint so that it can be accessed
class Complaints(models.Model):
    full_name = models.CharField(max_length=200)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    email = models.EmailField()
    state = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    subject = models.CharField(max_length=140)
    complaint = models.TextField()
    complaint_against = models.CharField(max_length=200)
    complaint_date = models.DateTimeField(auto_now_add=True)
    complaint_tag = models.CharField(max_length=200, default="")
    ticket_id = models.CharField(max_length=25, default=generate_key, unique=True)


    # TODO: Return Subject, Tags, Created date
    def __str__(self):
        return self.subject

    def get_complaint_tags(self):
        return self.complaint_tag.split(',')

    class Meta:
        verbose_name_plural = "Complaints"