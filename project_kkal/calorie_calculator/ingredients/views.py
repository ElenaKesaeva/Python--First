
from django.contrib.auth import login, authenticate
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from ingredients.forms import AuthenticationForm, RegisterForm
from ingredients.models import Ingredient, ItemConsumed
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView as LoginViewGeneric,
    LogoutView as LogoutViewGeneric,
)


def index(request: HttpRequest):
    context = {"ingredients": Ingredient.objects.order_by("pk").all()
               }
    return render(request=request, template_name='ingredients/index.html', context=context)


def register(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/ingredients')
    else:
        form = RegisterForm()
    return render(request=request, template_name='ingredients/register.html', context={'form': form})


class LoginView(LoginViewGeneric):
    form_class = AuthenticationForm
    next_page = reverse_lazy('ingredients:index')


class LogoutView(LogoutViewGeneric):
    next_page = reverse_lazy('ingredients:index')


def details(request: HttpRequest, pk: int):
    context = {"ingredient": get_object_or_404(Ingredient, pk=pk),
               }
    return render(request=request, template_name='ingredients/details.html', context=context)


def ingredient_outcome_view(request: HttpRequest):
    if request.method == 'POST':
        ingredients = Ingredient.objects.all()
        ingredient = request.POST['ingredient_consumed']
        ingredient_consumed = Ingredient.objects.get(name=ingredient)
        user = request.user
        outcome = ItemConsumed(user=user, ingredient_consumed=ingredient_consumed)
        outcome.save()

    else:
        ingredients = Ingredient.objects.all()

    user_outcome = ItemConsumed.objects.filter(user=request.user)

    total_calories = 0
    for item in user_outcome:
        total_calories += item.ingredient_consumed.calorie

    context = {'ingredients': ingredients, 'user_outcome': user_outcome, 'total_calories': total_calories}
    return render(request=request, template_name='ingredients/outcome.html', context=context)


def ingredient_delete(request: HttpRequest, ingredient_id):

    ingredient_consumed = ItemConsumed.objects.filter(id=ingredient_id)

    if request.method == 'POST':
        ingredient_consumed.delete()
        return redirect('/ingredients/outcome')

    return render(request=request, template_name='ingredients/ingredient_delete.html')
