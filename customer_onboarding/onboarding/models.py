from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CountryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    country = models.ForeignKey(CountryModel, on_delete=models.SET_NULL, null=True, blank=True)

#settings.AUTH_USER_MODEL = 'onboarding.CustomUser'

class DocumentSetModel(models.Model):
    name = models.CharField(max_length=100)
    countries = models.ManyToManyField(CountryModel)
    has_backside = models.BooleanField(default=False)
    ocr_labels = models.TextField()  # JSON string of labels

    def __str__(self):
        return self.name

class CustomerModel(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    nationality = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.surname}"

class CustomerDocumentModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    attached_file = models.FileField(upload_to='documents/')
    extracted_json = models.TextField()  # JSON string of extracted data
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.customer.firstname} {self.customer.surname}"
