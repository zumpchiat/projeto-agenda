from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.models import Contact
from contact.forms import ContactForm


def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form =ContactForm(request.POST)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
           # return redirect('contact:index')
            return redirect('contact:update', id=contact.pk )


        template = 'contact/pages/create.html'
        return render(request, template, context)
    

    context = {
            'form_action': form_action,
            'form': ContactForm()
        }
    template = 'contact/pages/create.html'
    return render(request, template, context)


def update(request, id):
    contact = get_object_or_404(Contact, id=id, show=True)
    form_action = reverse('contact:update', args=(id,))

    if request.method == 'POST':
        form =ContactForm(request.POST, instance=contact )
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
           # return redirect('contact:index')
            return redirect('contact:update', id=contact.pk )


        template = 'contact/pages/create.html'
        return render(request, template, context)
    

    context = {
            'form_action': form_action,
            'form': ContactForm(instance=contact)
        }
    template = 'contact/pages/create.html'
    return render(request, template, context)


