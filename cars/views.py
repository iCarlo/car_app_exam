from django.shortcuts import render, redirect
from .forms import CarsForm
from .models import Cars


def home_page(request):
    cars = Cars.objects.all().order_by('-date_created')
    colors = []
    for car in cars:
        colors.append(car.color)

    if request.POST:
        search = request.POST.get('search')
        if search in colors:
            cars = Cars.objects.filter(color=search).order_by('-date_created')
        else:
            cars = []
    context = {
        'cars': cars
    }
    return render(request, 'cars/home.html', context)


def create_page(request):
    form = CarsForm()
    if request.method == 'POST':
        form = CarsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'cars/create.html', context)
