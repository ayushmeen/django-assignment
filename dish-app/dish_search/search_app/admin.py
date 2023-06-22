from django.contrib import admin
from .models import Dish

class Display(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(Dish,Display)
