from rest_framework import viewsets, generics
from .models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosCursoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer    
    
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    def get_queryset(self):
        return Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    
    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosCurso(generics.ListAPIView):
    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk'])
    
    serializer_class = ListaAlunosCursoSerializer
