from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_view, name='category_view'),
]
