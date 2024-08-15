from django.contrib import admin
from contact.models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'phone', 'email', 'created_date',)
    ordering = ['-id']

    #list_filter = 'created_date',
    search_fields = 'id','first_name',
    list_per_page = 12
    list_max_show_all = 25
    list_editable = 'last_name', 'phone',
    list_display_links = 'first_name',

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'nome',

    