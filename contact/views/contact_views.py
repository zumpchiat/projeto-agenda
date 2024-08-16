from django.shortcuts import render, get_object_or_404
from contact.models import Contact
# Create your views here.
def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('-id')[:12]
    context = {
        'contacts': contacts
    }
    return render(
        request,
        'contact/pages/index.html',
         context 
    )

def contact(request, id):
    contact = get_object_or_404(Contact.objects.filter(show=True), pk=id)
    context = {
        'contact':contact
    }

    return render(
        request,
        'contact/pages/contact.html',
        context
    )
