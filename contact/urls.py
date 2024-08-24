
from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    
    
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    #Contact
    path('contact/<int:id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:id>/update/', views.update, name='update'),
    path('contact/<int:id>/delete/', views.delete, name='delete'),
]
