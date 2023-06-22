from search_app.models import Dish
import csv

with open('restaurants_small.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        Dish.objects.create(name=row[1])