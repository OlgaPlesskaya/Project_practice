from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(
        label="Загрузите файл",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
    )