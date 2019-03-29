from django.contrib import admin

# Register your models here.
from drinktaskerapp.models import Restaurant, Customer, Driver, Coffee

admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Coffee)
