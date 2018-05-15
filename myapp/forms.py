from django.forms import modelformset_factory, ModelForm, NumberInput
from djangoformsetjs.utils import formset_media_js
from .models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'color', 'body_style')

    class Media(object):
        js = formset_media_js


CarFormSet = modelformset_factory(Car, form=CarForm, can_delete=True)
