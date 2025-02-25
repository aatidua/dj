from django.db import models

# Create your models here.

class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)
    unit_price = models.CharField(max_length = 5)

    def __str__(self):
        return self.name
    
class MenuItems(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField( default= 0, max_digits=5, decimal_places=2) 

    def __str__(self):
        return self.title
        

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.DecimalField(default=0, max_digits=5,decimal_places=2)



    
class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE, default=0)
    timestamp = models.DateTimeField(auto_now_add=False, null=True)