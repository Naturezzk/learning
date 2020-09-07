from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Document
class IndexView(generic.ListView):
    template_name = 'autopicks/index.html'
    context_object_name = 'latest_Document_list'
    def get_queryset(self):
        """Return the last five published Documents."""
        return Document.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model = Document
    template_name = 'autopicks/detail.html'
class ResultsView(generic.DetailView):
    model = Document
    template_name = 'autopicks/results.html'

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
