from django.http import HttpResponseNotAllowed
from rest_framework import viewsets, status, generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from accounts.models import BlockList
from service.models import SystemInformation, Service
from service.models import Event
from service.models.booked_dates import BookedDates
# from service.models.history import History
from service.models.order import Order
from service.models.system_information import BaseImage
from service.models.wedding_hall import Menu, WeddingHall, MenuItem
# from service.serializers.history_serializers import HistorySerializer
from service.serializers.order_serializers import OrderPostSerializer, OrderGetSerializer
from service.serializers.service_serializers import ServiceSerializers
from service.serializers.system_information_serializers import SystemInformationSerializers, BaseImageSerializers
from service.serializers.events_serializers import EventSerializers

# Create your views here.

# class SystemInformationViewsets(viewsets.ModelViewSet):
#     queryset = SystemInformation.objects.all()
#     serializer_class = SystemInformationSerializers
#     # parsr_classes = [MultiPartParser, FormParser]

# class SystemInformationList(APIView):
#     def get(self, request, format=None):
#         systeminfo = SystemInformation.objects.all()
#         serializer = SystemInformationSerializers(systeminfo, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SystemInformationSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SystemInformationList(generics.ListCreateAPIView):
#     queryset = SystemInformation.objects.all()
#     serializer_class = SystemInformationSerializers
#
#
# class SystemInformationDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SystemInformation.objects.all()
#     serializer_class = SystemInformationSerializers
from service.serializers.wedding_hall_serializers import MenuSerializers, WeddingHallSerializers, MenuItemSerializers


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class SystemInfoView(generics.ListAPIView):
    queryset = SystemInformation.objects.all()
    serializer_class = SystemInformationSerializers
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventViews(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers
    permission_classes = [IsAdminUser]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class MenuView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers


class MenuItemView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers


class WeddingHallView(generics.ListAPIView):
    serializer_class = WeddingHallSerializers

    # def get_queryset(self):
    #     city = self.request.user.city
    #     date = self.request.user.event_date
    #     booked_dates = BookedDate.objects.filter(date=date).values_list('booked_dates_id', flat=True)
    #     if booked_dates.exists():
    #         restorans = RestoranModel.objects.all().exclude(id__in=booked_dates)
    #         return RestoranModel.objects.filter(id__in=restorans, city=city)
    #     return RestoranModel.objects.filter(city=city)

    def get_queryset(self):
        cite = self.request.user.cite
        date = self.request.user.wedding_date
        events_id = self.request.query_params.get("id")
        wedding_hall = WeddingHall.objects.filter(event=events_id).all()
        booked_dates = BookedDates.objects.filter(date=date).values_list('wedding_hall_id', flat=True)
        if booked_dates.exists():
            # restorans = WeddingHall.objects.all().exclude(id__in=booked_dates)
            restorans = wedding_hall.exclude(id__in=booked_dates)
            return WeddingHall.objects.filter(id__in=restorans, cite=cite)
        return wedding_hall.filter(cite=cite)


class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers


# class HistoryView(generics.ListAPIView):
#     queryset = History.objects.all()
#     serializer_class = HistorySerializer

class BaseImageview(generics.ListAPIView):
    queryset = BaseImage.objects.all()
    serializer_class = BaseImageSerializers


class OrderView(generics.ListAPIView):
    serializer_class = OrderGetSerializer
    # Order.service_price()
    queryset = Order.objects.all()

    def post(self, request):
        blacklist = BlockList.objects.all()
        blacklist = blacklist.values("user_id")
        user = self.request.user
        list = []
        for black in blacklist:
            list.append(black['user_id'])
        if user.id in list:
            return HttpResponseNotAllowed("not allowed")
        else:

            serializer = OrderPostSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['user'] = self.request.user
            total_price = 0
            menu = Menu.objects.get(pk=request.data.get("menu"))
            # people_count = request.data.get("people_count")

            services = Service.objects.filter(pk__in=request.data.get('service')).all()

            for service in services:
                total_price += service.price
            total_price += menu.price  # * people_count

            serializer.save(total_price=total_price)
            wedding_id = request.data.get('wedding_hall')
            wedding_id = WeddingHall.objects.get(id=wedding_id)
            wedding_date = self.request.user.wedding_date
            BookedDates.objects.create(date=wedding_date, wedding_hall=wedding_id)
            return Response(data=serializer.data)
