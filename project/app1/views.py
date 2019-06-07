from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import PersonForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
        else:
            render(request, 'formPersona.html', {'form': form})
    else:
        form = PersonForm
    return render(request, 'formPersona.html', {'form': form})