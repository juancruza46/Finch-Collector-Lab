from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Finch

# Create your testing finches here

#define home view
def home(request):
    return render(request, 'home.html')

#define about view
def about(request):
    return render(request, 'about.html')

#define finches index view 
def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

#define details view
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'




