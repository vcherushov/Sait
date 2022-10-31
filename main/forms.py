from django import forms
from .models import *
import django_filters


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'



class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['cat'].empty_label = "Номер не выбран"

    class Meta:
        model = Avtobus
        fields = ['door', 'time_create', 'time_time']
        widgets = {
            'time_create': DateInput(),
            'time_time': TimeInput(format='%H:%M')
        }




