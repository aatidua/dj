from django.shortcuts import render

# Create your views here.
from .models import Ingredients, MenuItems, RecipeRequirement
from django.views.generic import ListView, DetailView

class IngredientsList(ListView):
    model = Ingredients
    template_name = 'inventory/ingredients_list.html'

class MenuItemsList(ListView):
    model = MenuItems
    template_name = 'inventory/menu_items_list.html'

class RecipeRequirementList(ListView):
    model = RecipeRequirement
    template_name = 'inventory/recipe_requirement_list.html'

print(dir(ListView))