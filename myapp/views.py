from django.shortcuts import render
from .forms import CarFormSet

# Create your views here.
def manage_cars(request):
    if request.method == 'POST':
        formset = CarFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = CarFormSet()
    return render(request, 'myapp/myform.html', {'formset': formset})