from django.contrib import admin
from django.urls import path, include
from escola.views import AlunoViewSet, CursoViewSet, MatriculaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet, basename="Alunos")
router.register(r'cursos', CursoViewSet, basename="Cursos")
router.register(r'matriculas', MatriculaViewSet, basename="Matriculas")


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
