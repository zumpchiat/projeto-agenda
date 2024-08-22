from django.shortcuts import render, redirect
from contact.forms import ContactForm


def create(request):
    
    if request.method == 'POST':
        form =ContactForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:index')


        template = 'contact/pages/create.html'
        return render(request, template, context)
    

    context = {
            'form': ContactForm()
        }
    template = 'contact/pages/create.html'
    return render(request, template, context)