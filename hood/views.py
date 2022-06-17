from django.shortcuts import render
from django.contrib.auth.models import User
from hood.models import Neighbourhood
from hood.forms import *
# Create your views here.
def index(request):
    # return HttpResponse('Hi there')
    hoods = Neighbourhood.objects.all()
    return render(request, 'index.html', {"hoods": hoods})

def signup(request):
    print('here')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

