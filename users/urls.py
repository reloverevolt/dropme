from rest_framework.urlpatterns import format_suffix_patterns
from users.views import (
	UserDetailView,
	UserCreateView	
	)
from django.urls import path

urlpatterns = [
	path('<int:tid>/', UserDetailView.as_view(), name='user-detail'),
	path('create/', UserCreateView.as_view(), name='create-user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)