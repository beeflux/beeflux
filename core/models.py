from django.db import models


class Organization(models.Model):
    name = models.CharField("Organization Name", max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    established = models.DateTimeField(blank=True, null=True)

    class META:
        db_table = "organization"
        get_latest_by = ["-created_date"]
        ordering = ["-created_date"]
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return '%s %s' % (self.name, str(self.created_date))
