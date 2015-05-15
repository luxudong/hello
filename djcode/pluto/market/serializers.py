from rest_framework import serializers
from .models import Quote, Document

class QuoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quote
		fields = ('id', 'market', 'category','code','name',
			'opening', 'maximum', 'minimum','close','volume','amount','time')

class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = ('id','docfile')
			
								
		