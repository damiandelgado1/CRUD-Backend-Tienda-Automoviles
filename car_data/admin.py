from django.contrib import admin
from .models import Car

# View of the Data Car in the panel admin
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display=("brand", "model", "availability", "price")
    list_filter=("brand", "model")