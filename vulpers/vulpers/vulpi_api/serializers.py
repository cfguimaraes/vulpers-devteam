from rest_framework.serializers import ModelSerializer
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from .models import User

class UserSerializer(ModelSerializer):

	class Meta:
		model = User
		fields = '__all__'

class UserPagination(PageNumberPagination):
	page_size = settings.DEFAULT_PAGE_SIZE