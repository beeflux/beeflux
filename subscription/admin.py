from django.contrib import admin

# Register your models here.
from .models import Subscription, Package, Payment
admin.site.register(Subscription)
admin.site.register(Package)
admin.site.register(Payment)