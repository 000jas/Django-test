from rest_framework import serializers


class SignSerializer(serializers.Serializer):
	message = serializers.CharField()
	save = serializers.BooleanField(default=False)


class VerifySerializer(serializers.Serializer):
	message = serializers.CharField()
	signature = serializers.CharField()