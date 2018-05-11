from rest_framework import generics, status, response
from .models import Profissional
from .serializer import ProfissionalSerializer
import requests


class ProfissionaisList(generics.ListAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

    def post(self, request, format=None):
        serializer = ProfissionalSerializer(data=request.data)
        if serializer.is_valid():
            login = serializer.data.login
            # data_consumed_from_gh = self.consumirGitHubSearchApi(self, login)
            serializer.save()

            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def consumirGitHubSearchApi(self, login):
        result = self.conectionapi(login)
        return result

    def conectionapi(login):
        url = "https://api.github.com/search/users"
        payload = {"q": login, "type": "user", "in": "login"}
        r = requests.get(url, payload)
        data = r.json()
        return data
