"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from polls.models import Dataset,Supplier,Message,CategoryLvl,Author,PublicationPlace
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from polls import views

# Serializers define the API representation.
class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'
          
# ViewSets define the view behavior.
class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

# ПоставщикSerializers define the API representation.
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
          
# ViewSets define the view behavior.
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# Текстовое сообщение
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
          
# ViewSets define the view behavior.
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


#Категории
class CategoryLvlSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryLvl
        fields = '__all__'
          
# ViewSets define the view behavior.
class CategoryLvlViewSet(viewsets.ModelViewSet):
    queryset = CategoryLvl.objects.all()
    serializer_class = CategoryLvlSerializer

#Автор
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
          
# ViewSets define the view behavior.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

#Место публикации
class PublicationPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationPlace
        fields = '__all__'
          
# ViewSets define the view behavior.
class PublicationPlaceViewSet(viewsets.ModelViewSet):
    queryset = PublicationPlace.objects.all()
    serializer_class = PublicationPlaceSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'datasets', DatasetViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'categoryLvls', CategoryLvlViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'publicationplaces', PublicationPlaceViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project Title",
        default_version='v1',
        description="Тестовое описание",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snakesandrubies.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.home_view, name='home_view'),
    #path('home/', views.category_view, name='category_view'),
    #path('test/', views.upload_file, name='upload_file'),
    path('progress/', views.get_progress, name='get_progress'),
    path('download/<str:filename>/', views.download_file, name='download_file'),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
