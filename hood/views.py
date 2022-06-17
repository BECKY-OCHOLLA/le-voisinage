from django.shortcuts import render
from django.contrib.auth.models import User
from hood.models import Neighbourhood
# Create your views here.
def index(request):
    # return HttpResponse('Hi there')
    hoods = Neighbourhood.objects.all()
    return render(request, 'index.html', {"hoods": hoods})
