from django.conf.urls import url
from .views import List

urlpatterns = [
	url(r'^professional', List.as_view(), name='list')
]