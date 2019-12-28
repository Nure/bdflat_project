from django.contrib import admin

# Register your models here.
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'hire_date')
  list_display_links = ('name', 'id')
  search_fields = ('name',)
  list_max_show_all = 10

admin.site.register(Agent, AgentAdmin)
