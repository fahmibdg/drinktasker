from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from drinktaskerapp.forms import UserForm, RestaurantForm, UserFormForEdit, CoffeeForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from drinktaskerapp.models import Coffee

# Create your views here.
def home(request):
    return redirect(restaurant_home)

@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return redirect(restaurant_order)

@login_required(login_url='/restaurant/sign-in/')
def restaurant_account(request):
    user_form = UserFormForEdit(instance = request.user)
    restaurant_form = RestaurantForm(instance = request.user.restaurant)

    if request.method == "POST":
        user_form = UserFormForEdit(request.POST, instance = request.user)
        restaurant_form = RestaurantForm(request.POST, request.FILES, instance = request.user.restaurant)

        if user_form.is_valid() and restaurant_form.is_valid():
            user_form.save()
            restaurant_form.save()

    return render(request, 'restaurant/account.html', {
        "user_form": user_form,
        "restaurant_form": restaurant_form
    })

@login_required(login_url='/restaurant/sign-in/')
def restaurant_coffee(request):
    coffees = Coffee.objects.filter(restaurant = request.user.restaurant).order_by("-id")
    return render(request, 'restaurant/coffee.html', {"coffees": coffees})

@login_required(login_url='/restaurant/sign-in/')
def restaurant_add_coffee(request):
    form = CoffeeForm()

    if request.method == "POST":
        form = CoffeeForm(request.POST, request.FILES)

        if form.is_valid():
            coffee = form.save(commit=False)
            coffee.restaurant = request.user.restaurant
            coffee.save()
            return redirect(restaurant_coffee)

    return render(request, 'restaurant/add_coffee.html', {
        "form": form
    })

@login_required(login_url='/restaurant/sign-in/')
def restaurant_edit_coffee(request, coffee_id):
    form = CoffeeForm(instance = Coffee.objects.get("id = coffee_id"))

    if request.method == "POST":
        form = CoffeeForm(request.POST, request.FILES, instance = Coffee.objects.get(id = coffee_id))

        if form.is_valid():
            form.save()
            return redirect(restaurant_coffee)

    return render(request, 'restaurant/add_coffee.html', {
        "form": form
    })


@login_required(login_url='/restaurant/sign-in/')
def restaurant_order(request):
    return render(request, 'restaurant/order.html', {})

@login_required(login_url='/restaurant/sign-in/')
def restaurant_report(request):
    return render(request, 'restaurant/report.html', {})

def restaurant_sign_up(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        restaurant_form = RestaurantForm(request.POST, request.FILES)

        if user_form.is_valid() and restaurant_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_restaurant = restaurant_form.save(commit=False)
            new_restaurant.user = new_user
            new_restaurant.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect(restaurant_home)

    return render(request,'restaurant/sign_up.html',{
    "user_form": user_form,
    "restaurant_form": restaurant_form
    })
