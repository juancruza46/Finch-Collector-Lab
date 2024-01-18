from django.shortcuts import render
from .models import Finch

# Create your testing finches here
'''
finches = [
    {'name': 'finchy', 'color': 'white', 'description' : 'lazy finch does not fly' },
    {'name': 'isabelle', 'color': 'red', 'description' : 'flys high' },
]'''

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




