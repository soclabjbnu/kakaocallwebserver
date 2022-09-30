from django import forms

from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['last', 'first', 'born']
        labels = {
            'last': '성',
            'first': '이름',
            'born': '출생년도',
        }
