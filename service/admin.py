# from singleton_models.admin import SingletonModelAdmin
from django.contrib import admin
from .models import SystemInformation, Event, Service
from .models.system_information import SysteminfoImage, BaseImage
from .models.wedding_hall import Menu, MenuItem, WeddingHall
from .models.booked_dates import BookedDates
from .models.order import Order

# Register your models here.

admin.site.register(
    [SystemInformation, Event, Service, SysteminfoImage, Menu, MenuItem, WeddingHall, BookedDates, Order, BaseImage])
