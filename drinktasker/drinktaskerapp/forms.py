from django import forms

from django.contrib.auth.models import User
from drinktaskerapp.models import Restaurant, Coffee

#Class MealAdmin(admin.ModelAdmin):
    #list.display = ('name', 'restaurant', )
    #list.filter = ('restaurant,' )

    #admin.site.register(Restaurant)
    #admin.site.register(Customer)
    #admin.site.register(Driver)
    #admin.site.register(Meal, MealAdmin)
    #admin.site.register(Order)
    #admin.site.register(OrderDetails)

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ("name", "phone", "address", "logo")

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        exclude = ("restaurant",)
