from django.shortcuts import render
from django.http import HttpResponse
from .models import Dataset,Supplier,Message

def dataset_list(request):
    datasets = Dataset.objects.all()
    messages = Message.objects.all()
    return render(request, 'polls/dataset_list.html', {'datasets': datasets, 'messages': messages})

# Create your views here.
