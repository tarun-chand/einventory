from dataclasses import fields
from rest_framework import serializers
from einventoryAPI.models import ProductTypeMaster, BuildingMaster, Product_details, User_details, Section_details, Allotment_details


class ProductTypeMasterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductTypeMaster
        fields = "__all__"


class BuildingMasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuildingMaster
        fields = "__all__"


class Product_detailsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product_details
        fields = "__all__"


class User_detailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_details
        fields = "__all__"


class Section_detailsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Section_details
        fields = "__all__"


class Allotment_detailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allotment_details
        fields = "__all__"
