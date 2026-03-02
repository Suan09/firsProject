
from django.urls import path

from cars import views

app_name = 'cars'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:car_id>/', views.detail, name='detail'),
    path('create-car/', views.create_car, name='create_car'),
    path('ajax/load-models/', views.load_models, name='load_models'),
]