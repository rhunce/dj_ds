from django.shortcuts import render
from profiles.models import Profile
from django.http import JsonResponse
from .utils import get_report_image
from .models import Report
# from .forms import ReportForm #B
from django.views.generic import ListView, DetailView

# Create your views here.
class ReportListView(ListView):
  model = Report
  template_name = 'reports/main.html'

class ReportDetailView(DetailView):
  model = Report
  template_name = 'reports/detail.html'

def create_report_view(request):
  # form = ReportForm(request.POST or None) # B
  if request.is_ajax():
    name = request.POST.get('name') # A
    remarks = request.POST.get('remarks') # A
    image = request.POST.get('image')
    img = get_report_image(image)
    author = Profile.objects.get(user=request.user)

    # if form.is_valid(): # B
    #   instance = form.save(commit=False) # B
    #   instance.image = img # B
    #   instance.author = author # B
    #   instance.save() # B

    Report.objects.create(name=name, remarks=remarks, image=img, author=author) # A
    return JsonResponse({'msg': 'send'})
  return JsonResponse({})