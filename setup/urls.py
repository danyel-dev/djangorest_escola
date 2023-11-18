from django.contrib import admin
from django.urls import path, include
from escola.views import AlunoViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosCurso
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet, basename="Alunos")
router.register(r'cursos', CursoViewSet, basename="Cursos")
router.register(r'matriculas', MatriculaViewSet, basename="Matriculas")


urlpatterns = [
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosCurso.as_view()),
    path('admin/', admin.site.urls),
]
