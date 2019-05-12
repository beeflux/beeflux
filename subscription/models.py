from django.db import models
from django.contrib.auth.models import User


PACKAGE_CATEGORIES = (
    (1,'Free Trial'),
    (2,'Basic'),
    (3,'Business'),
    (4,'Professional')
)


class Package(models.Model):
    category = models.IntegerField(choices=PACKAGE_CATEGORIES, default=1)
    description = models.TextField(blank=True, null=True)
    pricing = models.FloatField(max_length=100)

    class Meta:
        db_table = 'package'

    def __str__(self):
        return str(self.category)    

class Subscription(models.Model):
    package = models.ForeignKey("package",related_name="subscriptions",on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=False, null=True)

    class Meta:
        get_latest_by = ['-priority', 'order_date']

    def __str__(self):
        return str(self.package)


class Payment(models.Model):
    subscription = models.ForeignKey("Subscription", related_name='subscription', on_delete=models.CASCADE)
    pay = models.FloatField()


