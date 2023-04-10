from django import forms
from .models import Contact


class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": 'section3__input',
            "placeholder": 'Антон',
        })
        self.fields['phone'].widget.attrs.update({
            "class": 'section3__input',
            "placeholder": 'Ваш телефон номер',
        })
        self.fields['descriptions'].widget.attrs.update({
            "class": 'section3__input',
            "placeholder": 'Оставьте сообщение',
        })
