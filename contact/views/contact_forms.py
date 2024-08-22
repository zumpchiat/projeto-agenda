from django.shortcuts import render
from contact.forms import ContactForm


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