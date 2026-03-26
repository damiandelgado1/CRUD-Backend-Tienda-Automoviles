from django.db import models

# Create new Car for Sales in the Shop
class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100, null=True)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    dimmenssion = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=3, decimal_places=2)
    tank = models.DecimalField(max_digits=3, decimal_places=2)
    consumption = models.DecimalField(max_digits=3, decimal_places=2)
    external_color = models.CharField(max_length=100, null=True)
    internal_color = models.CharField(max_length=100, null=True)
    availability = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        print(f"Marca {self.brand} | Modelo {self.model} | Availability {self.availability} | Price {self.price}")

    # Confirm create of the Car in the Shop
    def create_car(brand, model, engine, transmission, dimmenssion, weight, tank, consumption, external_color, internal_color, availability, price):
        car = Car.objects.create(
            brand=brand,
            model=model,
            engine=engine,
            transmission=transmission,
            dimmenssion=dimmenssion,
            weight=weight,
            tank=tank,
            consumption=consumption,
            external_color=external_color,
            internal_color=internal_color,
            availability=availability,
            price=price
        )

        print(f"Nuevo Auto a la venta {car.brand} {car.model}")

    # Modify data and specifications of the Car
    def modify_car(id, **kwargs):
        Car.objects.filter(id=id).update(**kwargs)
        print(f"Especificaciones del Auto {id} modificados")

    # Delete a Car in the Shop
    def delete_car(id):
        car = Car.objects.get(id=id)
        car.delete()

        print(f"Auto {car.brand} {car.model} eliminado")