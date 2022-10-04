from django.contrib import admin
from .models import House

admin.site.site_title = 'Real Estate'
admin.site.site_header = 'REAL ESTATE APPLICATION' 
admin .site.index_title = 'Real estate Houses'

# Register your models here.

admin.site.register(House)