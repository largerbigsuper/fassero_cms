from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms.widgets import Select

from .models import Article

class ArticleAdminForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': CKEditorUploadingWidget(),
        }
