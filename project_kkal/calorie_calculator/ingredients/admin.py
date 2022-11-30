
"""
The admin page
"""
from django.contrib import admin


from ingredients.models import Ingredient, User, ItemConsumed


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):

    list_display = "pk", "name", "protein", "fats", "carbohydrate", "calorie", "quantity"
    list_display_links = "pk", "name"


@admin.register(User)
class User(admin.ModelAdmin):

    list_display = "pk", "username", "email"
    list_display_links = "pk", "username"


@admin.register(ItemConsumed)
class ItemConsumed(admin.ModelAdmin):
    list_display = "user", "ingredient_consumed"
    list_display_links = "user", "ingredient_consumed"

