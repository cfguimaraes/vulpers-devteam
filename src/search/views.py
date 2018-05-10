
from rest_framework import generics
from .models import Profissional
from .serializer import ProfissionalSerializer


class ProfissionaisList(generics.ListCreateAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
