from rest_framework import serializers
from deals.models import Run
from users.serializers import UserSerializer


class RunListSerializer(serializers.ModelSerializer):

	user = serializers.SerializerMethodField()

	class Meta:
		model = Run
		fields = [
			'pk', 
			'user', 
			'geo_from', 
			'geo_to',
			'run_date',
			'transport',
			'status' 
			]

	def get_user(self, obj):
		return UserSerializer(obj.user, context=self.context).data	