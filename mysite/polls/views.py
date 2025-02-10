from django.shortcuts import render
from django.http import HttpResponse
from .models import Dataset

def dataset_list(request):
    datasets = Dataset.objects.all()
    return render(request, 'polls/dataset_list.html', {'datasets': datasets})

# Create your views here.
