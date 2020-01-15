from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Product

class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'detail': CKEditorUploadingWidget(),
        }
