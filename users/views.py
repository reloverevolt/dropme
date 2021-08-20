from rest_framework import generics, status, permissions
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer

class UserDetailView(APIView):
	def get(self, request, tid):
		try:
			user = User.objects.get(tid=tid)
			data = UserSerializer(user).data
			return Response(data, status=status.HTTP_200_OK)

			# add permission - telegram request only
		except ObjectDoesNotExist:
			msg = {'message': "object doesn't exist"}
			return Response(msg, status=status.HTTP_404_NOT_FOUND)	

class UserCreateView(APIView):
	serializer_class = UserSerializer
	def post(self, request):
		data = request.data
		serializer = self.serializer_class(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
