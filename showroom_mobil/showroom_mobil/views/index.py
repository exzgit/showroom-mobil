from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from showroom_mobil.models import Car, Service
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

def dashboard(request):
    total_mobil = Car.objects.count()
    total_service = Service.objects.count()
    total_cost_service = sum(service.cost for service in Service.objects.all())
    context = {
        'cars': Car.objects.all(),
        'total_mobil': total_mobil,
        'total_service': total_service,
        'total_cost_service': total_cost_service,
    }
    return render(request, 'dashboard.html', context)

def add_car(request):
    if request.method == 'POST':
        merk = request.POST.get('merk')
        model = request.POST.get('model')
        year = request.POST.get('year')
        base_price = request.POST.get('base_price')
        use_bank = request.POST.get('use_bank') == "on"
        loan = request.POST.get('loan') 
        interest_rate = request.POST.get('interest_rate')

        if merk and model and year and base_price:
            car = Car(
                merk=merk,
                model=model,
                year=year,
                use_bank=use_bank,
                base_price=base_price,
                loan=loan if use_bank else None,
                interest_rate=interest_rate if use_bank else None
            )
            car.save()
        
        return redirect('dashboard')

    return redirect(reverse('dashboard'))

def delete_car(request, id):
    car = get_object_or_404(Car, id=id)
    car.delete()
    return redirect(reverse('dashboard'))

def detail_car(request, id):
    car = get_object_or_404(Car, id=id)
    services = Service.objects.filter(car=car)
    context = {
        'car': car,
        'services': services,
    }
    return render(request, 'detail_car.html', context)



# Services 
def add_service(request, id):
    if request.method == 'POST':
        cost = request.POST.get('cost')
        date = request.POST.get('date')
        description = request.POST.get('description')
       

        if cost and date:
            service = Service(
                car=Car.objects.get(id=id),
                service_date=date,
                description=description,
                cost=cost
            )
            service.save()
        
    return redirect(reverse('detail_car', args=[id]))

def delete_service(request, id):
    service = get_object_or_404(Service, id=id)
    car_id = service.car.id
    service.delete()
    return redirect(reverse('detail_car', args=[car_id]))

def edit_car(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        car.merk = request.POST.get('merk')
        car.model = request.POST.get('model')
        car.year = request.POST.get('year')
        car.base_price = request.POST.get('base_price')
        car.use_bank = request.POST.get('use_bank') == "on"
        car.loan = request.POST.get('loan') 
        car.interest_rate = request.POST.get('interest_rate')

        if car.merk and car.model and car.year and car.base_price:
            car.save()
        
        return redirect(reverse('detail_car', args=[id]))

    return render(request, 'detail_car.html', {'car': car})


def edit_service(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        service.cost = request.POST.get('cost')
        service.service_date = request.POST.get('date')
        service.description = request.POST.get('description')

        if service.cost and service.service_date:
            service.save()
        
        return redirect(reverse('detail_car', args=[service.car.id]))

    return render(request, 'detail_car.html', {'service': service})