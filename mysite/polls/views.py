from django.shortcuts import render
from django.http import HttpResponse
from .models import Dataset,Supplier,Message,Category, Subcategory


def category_view(request):
    categories = Category.objects.all()
    return render(request, 'polls/index.html', {'categories': categories})
