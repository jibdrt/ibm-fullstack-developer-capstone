from django.contrib import admin
from .models import CarMake, CarModel


# Inline class to show CarModel within CarMake admin
class CarModelInline(admin.TabularInline):  # or admin.StackedInline for vertical layout
    model = CarModel
    extra = 1  # Number of empty CarModel forms to display by default


# Admin for CarModel (standalone view)
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'car_type', 'year', 'price')
    list_filter = ('car_make', 'car_type', 'year')
    search_fields = ('name',)


# Admin for CarMake, with inline CarModels
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year')
    search_fields = ('name', 'country')
    inlines = [CarModelInline]