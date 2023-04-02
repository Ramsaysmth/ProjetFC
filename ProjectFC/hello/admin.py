from django.contrib import admin

from .models import MainDataBase, ConfigDataBase, passWordDB, MatchingWordsDB

admin.site.register(ConfigDataBase)
admin.site.register(passWordDB)
#admin.site.register(MatchingWordsDB)

@admin.register(MainDataBase)
class MainDataBaseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'freqCard')
    ordering = ('nom',)
    search_fields = ('nom',)

@admin.register(MatchingWordsDB)
class MatchingWordsDB(admin.ModelAdmin):
    list_display = ('texte', 'reponse', 'iDTexte',)
    ordering = ('iDTexte',)
    search_fields = ('texte',)