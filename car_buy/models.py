from django.db import models
from car_data.models import Car
from decimal import Decimal

# Create new Buy by Client for get a Car
class BuyCar(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"El cliente {self.first_name} a comprado el auto {self.car}"

    # Consultation availability of the Vehicles
    @classmethod
    def consultation_car(cls, id):
        car = Car.objects.get(id=id)
        return f"Auto consultado: {car}"

    # Sample availability Car's in the Shop
    @classmethod
    def car_availability(cls, availability):
        car = Car.objects.filter(availability=availability)
        return f"Autos disponibles: {car}"

    # Buy a vehicle in the Shop
    @classmethod
    def buy_car(cls, brand_car, model_car, first_name, last_name):
        car = Car.objects.get(brand=brand_car, model=model_car)
        client = BuyCar.objects.create(first_name=first_name, last_name=last_name, car=car)
        price_buy = input("Ingrese el Dinero para comprar el auto")
        shop = Decimal(price_buy)

        if shop < car.price:
            return f"Dinero ingresado insuficiente. El auto vale {car.price}"
        elif shop > car.price:
            difference = shop - car.price
            return f"Auto comprado {car.brand} {car.model} por {client}. Te sobran ${difference}"
        else:
            return f"Auto comprado"