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

def results(request, Document_id):
    Document = get_object_or_404(Document, pk=Document_id)
    return render(request, 'autopicks/results.html', {'Document': Document})

def upload(request, Document_id):
    Document = get_object_or_404(Document, pk=Document_id)
    try:
        selected_choice = Document.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the Document uploading form.
        return render(request, 'autopicks/detail.html', {
            'Document': Document,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.uploads += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('autopicks:results', args=(Document.id,)))
