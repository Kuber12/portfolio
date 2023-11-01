import io,os
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, "index.html",{})

def contact(request):
    return render(request, "contact.html",{})

def download_pdf(request):
    file_name = "Kuber_cv.pdf"
    file_path = os.path.join(settings.BASE_DIR, 'theme/static', file_name)
    with open(file_path, 'rb') as fh:
        file_data = fh.read()
    response = FileResponse(file_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
    return response