from rest_framework import generics, status, permissions
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from deals.runs.serializers import RunListSerializer
from deals.models import Run



class RunListView(generics.ListAPIView):
	queryset = Run.objects.filter(is_opened=True).all()
	serializer_class = RunListSerializer

class RunDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Run.objects.filter(is_opened=True).all()
	serializer_class = RunListSerializer	
	lookup_field = 'pk'

class RunCreateView(generics.CreateAPIView):
	queryset = Run.objects.all()
	serializer_class = RunListSerializer
# ADD PERFORM CREATE (with supplied tid via header?)