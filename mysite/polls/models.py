from django.db import models
class Dataset(models.Model):
    identifier = models.AutoField(primary_key=True)   # Автоинкрементный идентификатор
    name = models.CharField(max_length=255)           # Наименование набора данных
    date = models.DateField()                         # Дата
    supplier_name = models.CharField(max_length=255)  # Наименование поставщика

def __str__(self):
        return f"Идентификатор: {self.identifier}, Наименование: {self.name}, Дата: {self.date}, Наименование поставщика: {self.supplier_name}"
# Create your models here.
