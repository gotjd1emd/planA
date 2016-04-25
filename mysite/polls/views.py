from django.shortcuts import render, get_object_or_404
from polls.models import Date
# Create your views here.
def index(request):
  last_day = Date.objects.all()
  return render(request, 'polls/index.html', {'last_day':last_day})

def blog(request, date_id):
  blog_content = get_object_or_404(Date, pk=date_id)
  return render(request, 'polls/blog.html', {'blog_content':blog_content})
