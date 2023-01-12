from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TravelingForm
from .models import Traveling
from django.template import loader


def Traveling_base(request):
  template = loader.get_template('Traveling_base.html')
  return HttpResponse(request, template.render())

# Adds function to views home page
def Traveling_home(request):
    # adds content of form to page
    return render(request, 'Traveling/Traveling_home.html')

def Traveling_create(request):
    form = TravelingForm(data=request.POST or None)
    if form.is_valid():
        form.save()  # Saves new contact
        return redirect('Traveling_home')
    else:
        print(form.errors)
    content = {'form': form}  # Pass content to the template in a dictionary
    # adds content of form to page
    return render(request, 'Traveling/Traveling_create.html', content)

def Traveling_read(request):
    travelers = Traveling.objects.all()
    content = {'travelers': travelers}
    # adds content of form to page
    return render(request, 'Traveling/Traveling_read.html', content)

# details search function
def Traveling_details(request, pk):
    traveler = get_object_or_404(Traveling, pk=pk)
    content = {'traveler': traveler}
    # adds content of form to page
    return render(request, 'Traveling/Traveling_details.html', content)


def Traveling_update(request, pk):
    entry = get_object_or_404(Traveling, pk=pk)
    form = TravelingForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'entry': entry}
    # adds content of form to page
    return render(request, 'Traveling/Traveling_update.html', content)

def Traveling_delete(request, pk):
    traveler = get_object_or_404(Traveling, pk=pk)
    if request.method == 'POST':
        traveler.delete()
        return redirect('../../read')
    content = {'traveler': traveler}
    # adds content of form to page
    return render(request, 'Traveling/Traveling_delete.html', content)