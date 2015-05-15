from rest_framework import serializers

from .models import Website

class WebsiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Website
		fields = ('id','url','category','is_dynamic','updated')

class PostWebsiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Website
		fields = ('id','url','updated')
			
		