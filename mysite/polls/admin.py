from django.contrib import admin
from .models import Dataset,Supplier,Message,CategoryLvl,Author,PublicationPlace,Category,Subcategory

admin.site.register(Dataset)
admin.site.register(Supplier)
admin.site.register(Message)
admin.site.register(CategoryLvl)
admin.site.register(Author)
admin.site.register(PublicationPlace)
admin.site.register(Category)
admin.site.register(Subcategory)


# Register your models here.
