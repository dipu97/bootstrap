from django.contrib import admin
from .models import Carousels
# Register your models here.


class CarouselAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    search_fields = ['title']


admin.site.register(Carousels, CarouselAdmin)
