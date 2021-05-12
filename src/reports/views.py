from django.shortcuts import render
from profiles.models import Profile
from django.http import JsonResponse
from .utils import get_report_image
from .models import Report
# from .forms import ReportForm #B
from django.views.generic import ListView, DetailView
# copied and pasted from https://xhtml2pdf.readthedocs.io/en/latest/usage.html
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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




# copied and pasted from https://xhtml2pdf.readthedocs.io/en/latest/usage.html
def render_pdf_view(request):
  template_path = 'reports/pdf.html'
  context = {'hello': 'Hello, World! From pdf...'}
  # Create a Django response object, and specify content_type as pdf
  response = HttpResponse(content_type='application/pdf')
  # if download
  # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
  # if display
  response['Content-Disposition'] = 'filename="report.pdf"'
  # find the template and render it.
  template = get_template(template_path)
  html = template.render(context)

  # create a pdf
  pisa_status = pisa.CreatePDF(
      html, dest=response)
  # if error then show some funy view
  if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
  return response