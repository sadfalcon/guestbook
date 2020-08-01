from django.contrib import admin
from .models import Card



class CardAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('pk', 'name', 'mail', 'text', 'created_at', 'updated_at')
    list_display_links = ('pk', 'name')
    search_fields = ('name',)


admin.site.register(Card, CardAdmin)