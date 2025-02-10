from django.urls import path

from .views import dataset_list

urlpatterns = [
    path('', dataset_list, name='dataset_list'),
]