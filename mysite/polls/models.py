from django.db import models
from django.core.validators import RegexValidator, EmailValidator, MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

class CategoryLvl(models.Model):
    identifier = models.AutoField(primary_key=True)  # Идентификатор
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"Категория: {self.name}"

class Author(models.Model):
    identifier = models.AutoField(primary_key=True)  # Идентификатор
    nickname = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    age = models.PositiveIntegerField()

    # Тип автора (можно использовать выбор из предопределенных значений)
    AUTHOR_TYPE_CHOICES = [
        ('Личный профиль', 'Личный профиль'),
        ('Сообщество', 'Сообщество')
    ]
    author_type = models.CharField(max_length=20, choices=AUTHOR_TYPE_CHOICES)
    
    # Пол автора
    GENDER_CHOICES = [
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
        ('Неизвестен', 'Неизвестен')
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    def __str__(self):
        return self.nickname

def validate_url(value):
    if not value.startswith(('http://', 'https://')):
        raise ValidationError('Ссылка должна начинаться с "http://" или "https://".')

class PublicationPlace(models.Model):
    identifier = models.AutoField(primary_key=True)  # Идентификатор
    name = models.CharField(max_length=255, unique=True)  # Наименование
    url = models.URLField(max_length=2048, validators=[validate_url])  # Ссылка

    def clean(self):
        # Проверка на то, что наименование не пустое
        if not self.name.strip():
            raise ValidationError('Наименование не должно быть пустым и должно содержать хотя бы один символ.')
    def __str__(self):
        return self.name


class Message(models.Model):
    identifier = models.AutoField(primary_key=True)  # Идентификатор
    text = models.TextField()  # Текст сообщения
    SOURCE_T = (
        ("Блоги", "Блоги"),
        ("Видео", "Видео"),
        ("Мессенджеры каналы", "Мессенджеры каналы"),
        ("Мессенджеры чаты", "Мессенджеры чаты"),
        ("Микроблоги", "Микроблоги"),
        ("Онлайн-СМИ", "Онлайн-СМИ"),
        ("Соцсети", "Соцсети"),
        ("Форумы", "Форумы"),
    )
    sourcetype = models.CharField(max_length=100, choices=SOURCE_T, blank=True)
    date = models.DateTimeField(auto_now_add=True)  # Дата публикации
    categories = models.ManyToManyField(CategoryLvl, help_text="Выберите классификацию/ии сообщения")  # Принадлежность классификатору
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Автор
    publication_place = models.ForeignKey(PublicationPlace, on_delete=models.CASCADE)  # Место публикации

    def __str__(self):
        return f"Идентификатор: {self.identifier}, Текст сообщения: {self.text}, Тип источника: {self.sourcetype} "

class Supplier(models.Model):
    # Поставщик
    identifier = models.AutoField(primary_key=True)   # Автоинкрементный идентификатор
    first_name = models.CharField(max_length=50, validators=[
        RegexValidator(regex=r'^[A-Za-zА-Яа-яЁё]+$', message='Имя должно содержать только буквы')
    ]) 
    last_name = models.CharField(max_length=50, validators=[
        RegexValidator(regex=r'^[A-Za-zА-Яа-яЁё]+$', message='Фамилия должна содержать только буквы')
    ])
    middle_name = models.CharField(max_length=50, validators=[
        RegexValidator(regex=r'^[A-Za-zА-Яа-яЁё]+$', message='Отчество должно содержать только буквы')
    ])
    position = models.CharField(max_length=100)  # должность
    phone = models.CharField(max_length=20, validators=[
        RegexValidator(regex = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', message='Неверный формат телефона. Пример: +7 (123) 456-78-90')
    ])
    email = models.EmailField(validators=[EmailValidator()])
    tg = models.CharField(max_length=50, blank=True, validators=[
        RegexValidator(regex=r'^@[A-Za-z0-9_]{5,}$', message='Неверный формат Telegram никнейма. Никнейм должен начинаться с @ и содержать минимум 5 символов.')
    ])
    def __str__(self):
        return f"Идентификатор: {self.identifier}, Имя: {self.first_name}"

class Dataset(models.Model):
    identifier = models.AutoField(primary_key=True)   # Автоинкрементный идентификатор
    name = models.CharField(max_length=255)           # Наименование набора данных
    date = models.DateField()                         # Дата
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)  # Внешний ключ на поставщика

    def __str__(self):
        return f"Идентификатор: {self.identifier}, Наименование: {self.name}, Дата: {self.date}, Наименование поставщика: {self.supplier}"
    def clean(self):
        # Проверка, что дата не в будущем
        if self.date > timezone.now().date():
            raise ValidationError('Дата не может быть в будущем')