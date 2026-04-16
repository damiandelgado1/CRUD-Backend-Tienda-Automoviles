# CRUD-Backend-Tienda-Automoviles

### description
This mini-project is a Backend CRUD for the Car Shop that manages the Car's for Sales and allow client purchase's a Car
<br>

### features
car_data app
- Create a new Car for Sales in the Shop
- Modify specifications a Car
- Delete a Car of the Shop

car_buy app
- Consultation a Car by ID
- Filter car's by the Availability
- Buy a car validation if a money with the Client pay of Car to buy is enough or insufficient

Connection with DataBase has in local with MySQL extension's in VSCode
<br>

### structure project

```text
car_shop/    # Project main
|
|-- car_data # App 1: Car Data e Information
|   |...
|
|-- car_buy  # App 2: Gestion de la Compra de Autos
|   |...
|
|-- data_base  # DataBase for storage data vehicle
|   |...
|
|-- manage.py
