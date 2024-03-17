from django import forms
from .models import EncryptedFile
class FileForm(forms.ModelForm):
    # class Meta:
    #     model = EncryptedFile
    #     fields = ['file']
# from django import forms

# class UploadFileForm(forms.Form):
    file = forms.FileField()
