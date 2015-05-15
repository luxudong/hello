from django.shortcuts import render
from .models import Website
from .serializers import WebsiteSerializer, PostWebsiteSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone


# Create your views here.
class WebsiteView(generics.ListCreateAPIView):
	serializer_class = WebsiteSerializer

	def get_queryset(self):
		return Website.objects.all()

	def get_paginate_by(self):
		return 20

	def post(self, request):
		import datetime
		serializer = PostWebsiteSerializer(
			data={
				"url":request.DATA.get('url'),
				"updated":datetime.datetime.now()
			}
		)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IndexView(views):
	def index(request):
		context={
			'last':"index",
		}
		return render(request,'index/index.html',context)
		