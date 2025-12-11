from django.contrib import admin

from galeria.models import Fotografia

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada') # Campos exibidos na lista de fotografias
    list_display_links = ('id', 'nome') # Campos que são links para a página de edição
    search_fields = ('nome', 'legenda') # Campos pesquisáveis
    list_filter = ('categoria',) # Filtros laterais
    list_per_page = 20 # Número de itens por página
    list_editable = ('publicada',) # Campos editáveis diretamente na lista
    ordering = ('id',) # Ordenação padrão

admin.site.register(Fotografia, FotografiaAdmin)