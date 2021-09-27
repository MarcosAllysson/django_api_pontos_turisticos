from django.contrib import admin
from comentarios.models import Comentario
from comentarios.actions import aprova_comentarios, reprova_comentarios


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'comentario', 'data', 'aprovado')
    actions = [aprova_comentarios, reprova_comentarios]
