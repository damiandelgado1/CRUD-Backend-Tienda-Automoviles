from django.db import models
from car_data.models import Car
from decimal import Decimal

# Create new Buy by Client for get a Car
class BuyCar(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    automobile = models.ForeignKey(Car, on_delete=models.CASCADE)

    # Consultation availability of the Vehicles
    def consultation_car(id):
        car = Car.objects.get(id=id)
        print(f"Auto consultado: {car}")

    # Sample availability Car's in the Shop
    def car_availability():
        car = Car.objects.filter(availability=True)
        print(f"Autos disponibles: {car}")

    # Buy a vehicle in the Shop
    def buy_car(id, first_name, last_name):
        car = Car.objects.get(id=id)
        client = BuyCar.objects.create(
            first_name=first_name,
            last_name=last_name
        )
        price_buy = input("Ingrese el Dinero para comprar el auto")
        shop = Decimal(price_buy)

        if shop < car.price:
            print(f"Dinero ingresado insuficiente. El auto vale {car.price}")
        elif shop > car.price:
            difference = shop - car.price
            print(f"Auto comprado {car.brand} {car.model} por {client}. Te sobran ${difference}")
        else:
            print(f"Auto comprado")