"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lead(models.Model):
    owner = models.ForeignKey(User)
    company = models.CharField(primary_key=True, max_length=100)
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.company + " " + self.status

class Contact(models.Model):
    title = models.CharField(max_length=100)
    phone = models.CharField(blank=True, max_length=20)
    direct = models.CharField(blank=True, max_length=20)
    fax = models.CharField(blank=True, max_length=20)
    cell = models.CharField(blank=True, max_length=20)
    lead = models.ForeignKey(Lead)
    def __str__(self):
        return self.title + " " + self.phone

class Note(models.Model):
    text = models.TextField()
    lead = models.ForeignKey(Lead)
    commenter = models.ForeignKey(User)
    def __str__(self):
        return self.lead.__str__() + " " + str(self.commenter) + " " + self.text

