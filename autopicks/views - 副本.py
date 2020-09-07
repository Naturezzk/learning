from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Document

def index(request):
    latest_document_list = Document.objects.order_by('-pub_date')[:5]
    context = {'latest_document_list': latest_document_list}
    return render(request, 'autopicks/index.html', context)

def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'autopicks/detail.html', {'document': document})

def results(request, document_id):
    response = "You're looking at the results of document %s."
    return HttpResponse(response % document_id)

def upload(request, document_id):
    return HttpResponse("You're uploading on document %s." % document_id)
