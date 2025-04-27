from django.shortcuts import render
from django.http import HttpResponse
from .models import Dataset,Supplier,Message,Category, Subcategory
import pandas as pd
import os
import re
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from .forms import FileUploadForm
from django.http import JsonResponse
import dask.dataframe as dd

def home_view(request):
    # Логика category_view
    categories = Category.objects.all()

    # Инициализация переменных для upload_file
    download_url = None
    error_message = None

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']

            # Создаем временную директорию
            temp_dir = os.path.join(settings.BASE_DIR, 'temp')
            os.makedirs(temp_dir, exist_ok=True)
            filepath = os.path.join(temp_dir, uploaded_file.name)

            # Сохраняем загруженный файл
            with open(filepath, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            try:
                # Обновляем прогресс: начало обработки
                request.session['progress'] = 10
                request.session.save()

                # Читаем файл в DataFrame
                df = pd.read_parquet(filepath)

                # Проверяем наличие столбца 'Текст'
                if 'Текст' not in df.columns:
                    error_message = "Столбец 'Текст' отсутствует в файле"
                    return render(request, 'polls/index.html', {'error_message': error_message})

                # Обновляем прогресс
                request.session['progress'] = 20
                request.session.save()

                # Чтение стоп-слов
                sw = pd.read_csv('/workspaces/Project_practice/mysite/stopwords-ru.txt')['c'].tolist()

                # Удаляем дубликаты и пустые строки
                df = df.drop_duplicates(subset='Текст')
                df = df[df['Текст'].notnull() & (df['Текст'].str.strip() != '')]

                # Приведение к нижнему регистру
                df['Текст'] = df['Текст'].str.lower()

                # Обновляем прогресс
                request.session['progress'] = 40
                request.session.save()

                # Обработка текста
                def process_text(text):
                    text = re.sub(r'\[.*?\]', '', text)
                    text = re.sub(r'@\w+', '', text)
                    text = re.sub(r'>>\d+(\s*\(.*?\))?', '', text)
                    text = re.sub(r'[^\w\s]', ' ', text)
                    text = re.sub(r'[^\w\s]|_', ' ', text)
                    text = re.sub(r'\d', '', text)
                    text = text.replace('ё', 'е')
                    text = ' '.join([word for word in text.split() if word not in sw])
                    return text

                df['О'] = df['Текст'].apply(process_text)

                # Удаление дубликатов в обработанном тексте
                df = df.drop_duplicates(subset='О')

                # Обновляем прогресс
                request.session['progress'] = 70
                request.session.save()

                # Сохранение обработанного файла
                processed_filename = "processed_file.csv"
                processed_filepath = os.path.join(temp_dir, processed_filename)
                df.to_csv(processed_filepath, index=False)

                # Генерация ссылки для скачивания
                download_url = f"/download/{processed_filename}/"
                
                # Логирование для проверки
                print("Сгенерированная ссылка:", download_url)

                # Обновляем прогресс: завершение
                request.session['progress'] = 100
                request.session.save()
                # Возвращаем JSON-ответ
                return JsonResponse({'download_url': download_url})

            except Exception as e:
                error_message = f"Ошибка при обработке файла: {str(e)}"

    else:
        form = FileUploadForm()
        

    # Возвращаем контекст для отображения
    return render(request, 'polls/index.html', {
        'categories': categories,
        'form': form,
        'download_url': download_url,
        'error_message': error_message,
    })


def get_progress(request):
    progress = request.session.get('progress', 0)
    return JsonResponse({'progress': progress})

# Скачивание обработанного файла
def download_file(request, filename):
    temp_dir = os.path.join(settings.BASE_DIR, 'temp')
    filepath = os.path.join(temp_dir, filename)

    if os.path.exists(filepath):
        with open(filepath, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    else:
        raise Http404("Файл не найден")

