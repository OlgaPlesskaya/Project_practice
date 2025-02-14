from django.contrib import admin
from .models import Dataset,Supplier,Message,CategoryLvl,Author,PublicationPlace

admin.site.register(Dataset)
admin.site.register(Supplier)
admin.site.register(Message)
admin.site.register(CategoryLvl)
admin.site.register(Author)
admin.site.register(PublicationPlace)


# Register your models here.
