from django.contrib import admin
from django.urls import path, include
from escola.views import AlunoViewSet, CursoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet, basename="Alunos")
router.register(r'cursos', CursoViewSet, basename="Cursos")


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
