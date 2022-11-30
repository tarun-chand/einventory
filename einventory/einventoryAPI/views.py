from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from einventoryAPI.models import ProductTypeMaster, BuildingMaster, Product_details, User_details, Section_details, Allotment_details
from einventoryAPI.serializers import ProductTypeMasterSerializer, BuildingMasterSerializer, Product_detailsSerializer, User_detailsSerializer, Section_detailsSerializer, Allotment_detailsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


def home_page(request):
    template = loader.get_template("index.html")
    res = template.render({}, request)
    return HttpResponse(res)


class ProductTypeMasterViewSet(viewsets.ModelViewSet):
    queryset = ProductTypeMaster.objects.all()
    serializer_class = ProductTypeMasterSerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        try:
            type = ProductTypeMaster.objects.get(pk=pk)
            product = Product_details.objects.filter(ProductTypeMaster=type)
            product_ser = Product_detailsSerializer(
                product, many=True, context={'request': request})
            return Response(product_ser.data)
        except Exception as e:
            return Response({'message': str(e)})


class BuildingMasterViewSet(viewsets.ModelViewSet):
    queryset = BuildingMaster.objects.all()
    serializer_class = BuildingMasterSerializer


class Product_detailsViewSet(viewsets.ModelViewSet):
    queryset = Product_details.objects.all()
    serializer_class = Product_detailsSerializer


class User_detailsViewSet(viewsets.ModelViewSet):
    queryset = User_details.objects.all()
    serializer_class = User_detailsSerializer


class Section_detailsViewSet(viewsets.ModelViewSet):
    queryset = Section_details.objects.all()
    serializer_class = Section_detailsSerializer


class Allotment_detailsViewSet(viewsets.ModelViewSet):
    queryset = Allotment_details.objects.all()
    serializer_class = Allotment_detailsSerializer
