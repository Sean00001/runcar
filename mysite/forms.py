from django import forms
from .models import Photo
class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        # fields = ('image','name',)
        # fields = ('image',)
        # exclude = ('car',)
        # fields = ('image',
        #           'car',)
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            # 'test': forms.TextInput(attrs={'class': 'form-control'})

            # 'name': forms.TextInput(attrs={'class': 'form-control-file'})

            # 'image': forms.FileInput(attrs={'multiple': True})

        }