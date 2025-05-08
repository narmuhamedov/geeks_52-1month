from django.shortcuts import render
from . import models

#Все продукты
def all_products_view(request):
  if request.method == 'GET':
    all_products = models.Product.objects.all().order_by('-id')
    context = {
      'all_products': all_products,
    }
    return render(request, template_name='tags/all_products.html', context=context)


#Еда
def meal_view(request):
  if request.method == 'GET':
    meal = models.Product.objects.all().order_by('-id').filter(tags__name='#Еда')
    context = {
      'meal': meal,
    }
    return render(request, template_name='tags/meals.html', context=context)
