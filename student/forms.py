from django.forms import ModelForm
from django.apps import apps
Detail = apps.get_models('home', 'Detail')


class CustomerForm(ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'
        exclude = ['user']


