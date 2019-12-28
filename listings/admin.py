from django.contrib import admin

# Register your models here.
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'agent', 'is_published', 'price', 'city', 'list_date')
  list_display_links = ('id', 'title')
  list_editable = ('agent', 'is_published')
  list_filter = ('agent',)
  search_fields = ('city', 'title', 'price',)
  list_per_page = 20

admin.site.register(Listing, ListingAdmin)