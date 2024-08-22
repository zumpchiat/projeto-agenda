from django.shortcuts import render

from contact.models import Contact

from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone', 'email',

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )

        )

def create(request):
    
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
        template = 'contact/pages/create.html'
        return render(request, template, context)
    

    context = {
            'form': ContactForm()
        }
    template = 'contact/pages/create.html'
    return render(request, template, context)