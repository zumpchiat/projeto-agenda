from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q

def index(request):
    contacts = Contact.objects \
        .all() \
        .filter(show=True)\
        .order_by('-id')[:12]
    
    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }
                                                                 
    return render(
        request,
        'contact/pages/index.html',
         context 
    )

def search(request):

    
    search_value = request.GET.get('q', '').strip()
    if(search_value == ''):
        return redirect('contact:index')

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(email__icontains=search_value) |
            Q(phone__icontains=search_value) 
            )\
        .order_by('-id')
    
   
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
