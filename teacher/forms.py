from django import forms
from .models import Upload_video,Upload_file
from django.apps import apps
detail = apps.get_model('home', 'Detail')

class Video_form(forms.ModelForm):
    class Meta:
        model = Upload_video
        fields = '__all__'

class Upload_form(forms.ModelForm):
    class Meta:
        model = Upload_file
        fields = '__all__'

class Edit(forms.ModelForm):
    class Meta:
        model = detail
        fields = ['image']