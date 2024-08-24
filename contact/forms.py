from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact

class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                    'email', 'description','category',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class':'classe-a classe-b',
                    'placeholder':'Digite o nome'
                }
            )
            
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:  
            self.add_error(
                'first_name',
                ValidationError(
                    'Ops!! Primeiro nome igual ao sobrenome.',
                    code='invalid'
                )

            )
        return super().clean()