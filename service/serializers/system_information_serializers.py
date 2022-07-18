from rest_framework import serializers
from service.models import SystemInformation

# class SystemInformationSerializers(serializers.ModelSerializer):
#     # system_information = serializers.PrimaryKeyRelatedField(
#     #     many=True, queryset=SystemInformation.objects.all())
#
#     class Meta:
#         model = SystemInformation
#         fields = ["id", "name", "type", "description"]
from service.models.system_information import SysteminfoImage, BaseImage


class SysteminfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysteminfoImage
        fields = '__all__'


class SystemInformationSerializers(serializers.HyperlinkedModelSerializer):
    images = SysteminfoImageSerializer(source='systeminfoimage_set', many=True, read_only=True)

    class Meta:
        model = SystemInformation
        fields = ["id", "name", "type", "description", 'images']

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        system_info = SystemInformation.objects.create(name=validated_data.get('name', 'no-title'),
                                                       type=validated_data.get('type', 'no-type'),
                                                       description=validated_data.get('description', 'no-description'))
        for image_data in images_data.values():
            SysteminfoImage.objects.create(system_info=system_info, image=image_data)

        return system_info


class BaseImageSerializers(serializers.ModelSerializer):
    class Ment:
        model = BaseImage
        system_info = ['id', 'image', 'title']
