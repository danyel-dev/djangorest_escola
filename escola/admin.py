from django.contrib import admin
from .models import Aluno, Curso, Matricula


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_field = ('nome',)
    list_per_page = 10
    
    
admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'nivel')
    list_display_links = ('id', 'codigo_curso')
    search_field = ('codigo_curso',)


admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'periodo')
    list_display_links = ('id', 'periodo')
    list_per_page = 10
    
    
admin.site.register(Matricula, Matriculas)
