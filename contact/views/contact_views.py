from django.shortcuts import render, get_object_or_404
from contact.models import Contact
# Create your views here.
def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('-id')[:12]
    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }
    return render(
        request,
        'contact/pages/index.html',
         context 
    )

def contact(request, id):
    contact = get_object_or_404(
        Contact.objects.filter(show=True), pk=id
        )
    contact_name = f'{contact.first_name} {contact.last_name} - '
    context = {
        'contact':contact,
        'site_title': contact_name
    }

    return render(
        request,
        'contact/pages/contact.html',
        context
    )
