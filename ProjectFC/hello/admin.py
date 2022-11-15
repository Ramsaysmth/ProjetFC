from django.contrib import admin

from .models import MainDataBase, ConfigDataBase

#admin.site.register(MainDataBase)
admin.site.register(ConfigDataBase)

@admin.register(MainDataBase)
class MainDataBaseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'freqCard')
    ordering = ('nom',)
    search_fields = ('nom',)