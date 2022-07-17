from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (SystemInfoView, EventViews, MenuView, WeddingHallView, ServiceView, MenuItemView, OrderView)

router = DefaultRouter()
router.register('system', SystemInfoView)
router.register('event', EventViews)
router.register('menu', MenuView)
# router.register('wedding_hall', WeddingHallView)
router.register('services', ServiceView)
router.register('menu_items', MenuItemView)
# router.register('order', OrderView)


urlpatterns = [
    # path("system/", SystemInformationList.as_view(), name='system'),
    # path("system/<int:pk>/", SystemInformationDetail.as_view(), name='syste'),
    # path('', include(router.urls)),
    path("system/", SystemInfoView.as_view()),
    path("event/", EventViews.as_view()),
    path("menu/", MenuView.as_view()),
    path("services/", ServiceView.as_view()),
    path("menu_items/", MenuItemView.as_view()),
    path('wedding_hall/', WeddingHallView.as_view()),
    path('order/', OrderView.as_view()),



]
