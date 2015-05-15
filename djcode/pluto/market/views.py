from django.shortcuts import render
from rest_framework import generics
from .models import Quote, Document
from .serializers import QuoteSerializer, DocumentSerializer

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from .forms import DocumentForm
from django.template import RequestContext


# Create your views here.

class QuoteView(generics.ListCreateAPIView):
	serializer_class = QuoteSerializer

	def get_queryset(self):
		return Quote.objects.all()

	def get_paginate_by(self):
		return 20

class DocumentView(generics.ListCreateAPIView):
	serializer_class = DocumentSerializer

	def get_queryset(self):
		return Document.objects.all()

	def get_paginate_by(self):
		return 20

def list(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()

			return HttpResponseRedirect(reverse('market.views.list'))
		else:
			form = DocumentForm()

		documents = Document.objects.all()

		return render_to_response(
			'security/list.html',
			{'documents':documents,'form': form},
			context_instance=RequestContext(request)

		)
			
		
		