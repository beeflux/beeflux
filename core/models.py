from django.db import models


class Organization(models.Model):
    name = models.CharField("Organization Name", max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    established = models.DateTimeField(blank=True, null=True)
