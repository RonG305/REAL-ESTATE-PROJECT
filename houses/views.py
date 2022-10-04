from django.shortcuts import render, redirect
from .models import House
from django.http import HttpResponse
from houses.forms import HouseForm

# Create your views here.

def Houses(request):
    houses = House.objects.all()
    context = {
        'houses': houses
    }

    return render(request, 'houses/index.html', context)

def add_house(request):
    form = HouseForm()
    if request.method == 'POST':  
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {
        'form': form
    }
    return render(request, 'houses/add_house.html', context)     


def update_house(request, pk):
    house = House.objects.get(id=pk)
    form = HouseForm(instance=house)
    if request.method == 'POST':  
        form = HouseForm(request.POST, instance=house, files = request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {
        'form': form
    }   
    return render(request, 'houses/update_house.html', context)   


def delete_house(request, pk):
    house = House.objects.get(id=pk)
    house.delete()
    

    context = {
        'house': house
    }  

    return render(request, 'houses/delete.html', context)

        




