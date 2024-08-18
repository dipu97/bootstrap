import re
from django.shortcuts import render
from .models import Carousels
# Create your views here.


def index(request):
    carousel_data = Carousels.objects.all()
    context = {
        'carousel_data': carousel_data
    }
    return render(request, 'index.html', context)


def footer(request):
    return render(request, 'pages/footer.html')
