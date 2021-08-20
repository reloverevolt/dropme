from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['pk', 'tid', 'name', 'nickname', 'lang', 'karma']

	def validate(self, data):
		tid = data.get('tid', None)
		if not tid:
			raise serializers.ValidationError("tid is requred")
		if User.objects.filter(tid=data['tid']).exists():
			raise serializers.ValidationError("user already exists")
		return data	
