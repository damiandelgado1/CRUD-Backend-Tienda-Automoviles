from django.contrib import admin
from .models import BuyCar

# View of the Data Car in the panel admin
@admin.register(BuyCar)
class BuyCarAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name", "automobile")
    list_filter=("first_name", "automobile")