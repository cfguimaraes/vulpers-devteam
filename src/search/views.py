# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
import requests

  	
class SearchGetView(APIView):


	def get(self, request):
		
		language = request.GET.get('language')
		location = request.GET.get('location')

		filter_language = self.stripparameter(language)
		filter_location = self.stripparameter(location)

		get_return_github = self.conectionapi(filter_language, filter_location)
		newjson = self.iteration_json(get_return_github['items'])
		return Response({"data": newjson})


	def stripparameter(self, param):

		strip_variable = param.replace(" ", "-")
		return strip_variable


	def conectionapi(request, language, location):

		url = "https://api.github.com/search/users?q=language:"+language+"+location:"+location+"&type=Users"
		r = requests.get(url)
		data = r.json()
		return data


	def iteration_json(self, data):
       
		datajson = []
		for name in data:
			login_arr = {}
			login_arr['login'] = name['login']
			login_arr['foto'] = name['avatar_url']
			login_arr['classificacao'] = self.is_jedi(name['score'])
			datajson.append(login_arr)
		return datajson


	def is_jedi(self, score):
		if score >= 3.5:
			get_type = "cavaleiro jedi"
		else:
		   get_type = "aprendiz jedi"

		return get_type