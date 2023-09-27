from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Consingment

admin.site.register(Customer)
admin.site.register(Consingment)
