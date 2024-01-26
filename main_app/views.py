from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'


class FinchUpdate(UpdateView):
    model = Finch
    # let's make it so you can't rename a cat
    # we could simply say fields = '__all__', or we can customize like this:
    fields = ['color', 'description', 'age']

# Delete View - extends DeleteView
class FinchDelete(DeleteView):
    model = Finch

    success_url = '/finches'

# this is to add a feeding
def add_feeding(request, finch_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # it's also important to validate forms.
    # django gives us a built in function for that
    if form.is_valid():
        # dont want to save the feeding to the db until we have a finch id
        new_feeding = form.save(commit=False)
        # this is where we add the finch
        new_feeding.finch_id = finch_id
        new_feeding.save()
    #redirect
    return redirect('detail', finch_id=finch_id)