from rest_framework import serializers

from service.models.wedding_hall import Menu, MenuItem, WeddingHall


class MenuItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ("name", "menu_id")


class MenuSerializers(serializers.ModelSerializer):
    menu_items = MenuItemSerializers(many=True)
    # menu_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ["id", "type", "price", "image", "menu_items", "wedding_hall_id"]

    def create(self, validated_data):
        menu_items_data = validated_data.pop("menu_items")
        menu = Menu.objects.create(**validated_data)
        #  type=validated_data.get('type', 'no-type'),
        # price=validated_data.get('price', 'no-price'),
        # # image=validated_data.get('image', 'no-image')
        # # menu_item=validated_data.get("menu_item", "no-menu-item"),
        # wedding_hall=validated_data.get("wedding_hall", "no-wedding_hall")
        # )
        for menu_item_data in menu_items_data:
            MenuItem.objects.create(menu=menu, **menu_item_data)
        return menu


class WeddingHallSerializers(serializers.ModelSerializer):
    # menus = MenuSerializers(many=True)
    menus = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = WeddingHall
        fields = ["id", "name", "address", "cite", "image", "menus", "event"]

    def create(self, validated_data):
        menus_data = validated_data.pop("menus")
        wedding_hall = WeddingHall.objects.create(**validated_data)
        for menu_data in menus_data:
            menu_items_data = menu_data.pop("menu_items")
            menu = Menu.objects.create(wedding_hall=wedding_hall, **menu_data)
            for menu_item_data in menu_items_data:
                MenuItem.objects.create(menu=menu, **menu_item_data)
        return wedding_hall

    # def update(self, instance, validated_data):
    #     menus_data = validated_data.pop("menus")
    #     menus = instance.menus.all()
    #     menus = list(menus)
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.address = validated_data.get("address", instance.address)
    #     instance.district = validated_data.get("district", instance.district)
    #     instance.image = validated_data.get("image", instance.image)
    #     instance.save()
    #
    #     for menu_data in menus_data:
    #         menu_items_data = menu_data.pop('menu_items')
    #         items = instance.menus.get().menu_items.all()
    #         items = list(items)
    #         for menu_item_data in menu_items_data:
    #             item = items.pop(0)
    #             item.name = menu_item_data.get('name', item.name)
    #             item.save()
    #         menu = menus.pop(0)
    #         menu.type = menu_data.get("type", menu.type)
    #         menu.price = menu_data.get('price', menu.price)
    #         menu.save()
    #     return instance

    # def update(self, instance, validated_data):
    #     menus_data = validated_data.pop('menus')
    #     menus = instance.menus.all()
    #     menus = list(menus)
    #     instance.wedding_hall = validated_data.get('wedding_hall', instance.wedding_hall)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.save()
    #
    #     for menu_data in menus_data:
    #         menuitems_data = menu_data.pop('menuitems')
    #         items = instance.menus.get().menuitems.all()
    #         items = list(items)
    #         for menuitem_data in menuitems_data:
    #             item = items.pop(0)
    #             item.itam_name = menuitem_data.get('itam_name', item.itam_name)
    #             item.image = menuitem_data.get('image', item.image)
    #             item.save()
    #         menu = menus.pop(0)
    #         menu.type = menu_data.get('type', menu.type)
    #         menu.price = menu_data.get('price', menu.price)
    #         menu.save()
    #     return instance
