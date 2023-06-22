from django.shortcuts import render
from .models import Dish

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Dish.objects.filter(name__icontains=query)
    return render(request, 'search.html', {'results': results, 'query': query})
