from django.shortcuts import render
from contact.forms import RegisterForm

def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            


    context ={
        'form': form
        }

    template = 'contact/pages/register.html'
    return render(request, template, context)
