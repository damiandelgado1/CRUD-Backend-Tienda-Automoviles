from django.db import models

# Create new Car for Sales in the Shop
class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100, null=True)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    dimmenssion = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    tank = models.DecimalField(max_digits=6, decimal_places=2)
    consumption = models.DecimalField(max_digits=6, decimal_places=2)
    external_color = models.CharField(max_length=100, null=True)
    internal_color = models.CharField(max_length=100, null=True)
    availability = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Marca {self.brand} | Modelo {self.model} | Availability {self.availability} | Price {self.price}"

    # Confirm create of the Car in the Shop
    def create_car(brand, model, engine, transmission, dimmenssion, weight, tank, consumption, external_color, internal_color, availability, price):
        car = Car.objects.create(brand=brand,model=model, engine=engine, transmission=transmission, dimmenssion=dimmenssion, weight=weight, tank=tank, consumption=consumption, external_color=external_color, internal_color=internal_color, availability=availability, price=price)

        car.save()

        return f"Nuevo Auto a la venta {car}"

    # Modify data and specifications of the Car
    def modify_car(id):
        car = Car.objects.filter(id=id)
        color = input("Indique el Nuevo Color del auto: ")
        car.external_color = color
        car.update()
        return f"Especificaciones del Auto {car} modificados"

    # Delete a Car in the Shop
    def delete_car(id):
        car = Car.objects.get(id=id)
        car.delete()

        return f"Auto {car.brand} {car.model} eliminado"