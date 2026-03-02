from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from cars.models import Brand, Car, CarModel, Fuel, Transmission
from users.models import User



def index(request):
    cars = Car.objects.select_related(
        "brand",
        "model",
        "fuel",
        "transmission"
    )

    brand_id = request.GET.get('brand')
    model_id = request.GET.get('model')
    fuel_id = request.GET.get('fuel')
    transmission_id = request.GET.get('transmission')

    if brand_id:
        cars = Car.objects.filter(brand_id=brand_id)
    if model_id:
        cars = Car.objects.filter(model_id=model_id)
    if fuel_id:
        cars = Car.objects.filter(fuel_id=fuel_id)
    if transmission_id:
        cars = Car.objects.filter(transmission_id=transmission_id)

    brands = Brand.objects.all()
    models = CarModel.objects.all()
    transmissions = Transmission.objects.all()
    fuels = Fuel.objects.all()

    paginator = Paginator(cars, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    query_params = request.GET.copy()
    if 'page' in query_params:
        del query_params['page']  # Удаляем страницу, чтобы она не дублировалась

    context = {
        'page_obj': page_obj,
        'brands': brands,
        'models': models,
        'transmissions': transmissions,
        'fuels': fuels,
        'filter_params': query_params.urlencode()
    }

    return render(request, 'cars/cars_list.html', context=context)


def detail(request, car_id):
    car = Car.objects.filter(pk=car_id).first()
    user_id = car.user_id
    user = User.objects.filter(pk=user_id).first()
    context = {
        'car': car,
        'user': user,
    }
    return render(request, 'cars/detail.html', context=context)


@login_required(login_url=reverse_lazy('users:login'), redirect_field_name=None)
def create_car(request):

    if request.method == 'POST':
        brand_id = request.POST.get('brand')
        model_id = request.POST.get('model')
        transmission_id = request.POST.get('transmission')
        fuel_id = request.POST.get('fuel')
        price = request.POST.get('price')
        mileage = request.POST.get('mileage')
        year = request.POST.get('year')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        user = request.user

        if not all([brand_id, model_id, fuel_id, transmission_id, year, price, mileage]):
            return HttpResponse("Все поля обязательны")
        
        Car.objects.create(
            brand_id = brand_id,
            model_id = model_id,
            transmission_id = transmission_id,
            fuel_id = fuel_id,
            price = price,
            mileage = mileage,
            year = year,
            description = description,
            image = image, 
            user=user,
        )
        return redirect('/')
    
    else:
        brands = Brand.objects.all()
        transmissions = Transmission.objects.all()
        fuels = Fuel.objects.all()
        context = {
            'brands': brands,
            'transmissions': transmissions,
            'fuels': fuels
        }
        return render(request, 'cars/create.html', context=context)


def load_models(request):
    brand_id = int(request.GET['brand_id'])
    models = CarModel.objects.filter(brand_id=brand_id).values('name', 'id')
    return JsonResponse(list(models), safe=False)




