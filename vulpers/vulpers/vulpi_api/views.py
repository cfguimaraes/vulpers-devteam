from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, UserPagination
from django.http import HttpResponse
import requests
import json

class List(APIView):
	def get(self, request):
		username = request.GET.get('username')

		if username is None:
			username = 'junior'
		url = "https://api.github.com/search/users?q="+username+"in:login"

		result = requests.get(url).json()

		users = []

		for data in result['items']:
			user = User()
			user.username = data['login']
			if data['score'] < 3.5:
				user.descricao = 'Aprendiz Jedi'
			else:
				user.descricao = 'Cavaleiro Jedi'

			users.append(user)
		serializer = UserSerializer(data=users, many=True)
		serializer.is_valid()
		return HttpResponse(json.dumps(serializer.data))
