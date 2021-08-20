from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from deals.runs.views import (
	RunListView,
	RunDetailView,
	RunCreateView	
	)


urlpatterns = [
	path('runs/', RunListView.as_view(), name='run-list'),
	path('runs/<int:pk>/', RunDetailView.as_view(), name='run-detail'),
	path('runs/create/', RunCreateView.as_view(), name='run-create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)