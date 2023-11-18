from rest_framework import viewsets, generics, authentication, permissions
from .models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosCursoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer    
    authentication_class = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_class = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_class = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    def get_queryset(self):
        return Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    
    serializer_class = ListaMatriculasAlunoSerializer

    authentication_class = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListaAlunosCurso(generics.ListAPIView):
    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk'])
    
    serializer_class = ListaAlunosCursoSerializer

    authentication_class = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
