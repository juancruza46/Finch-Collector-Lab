from django.shortcuts import render

# Create your views here.

#define home view
def home(request):
    return render(request, 'home.html')

#define about view

def about(request):
    return render(request, 'about.html')