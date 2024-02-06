from django.shortcuts import render, redirect
from .forms import BusForm
from .models import Bus

# Create your views here.
def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})
def add_bus(request):
    if request.method == "POST":
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = BusForm()
    return render(request, 'add_bus.html', {'form': form})
