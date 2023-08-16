from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializer import CustomerSerializer 
from .models import Customer
from rest_framework.views import APIView

@api_view(['GET'])
def ShowAll(request):
    Customers = Customer.objects.all()
    serializer = CustomerSerializer(Customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request, pk):
    Customers = Customer.objects.get(custId=pk)
    serializer = CustomerSerializer(Customers, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    serializer = CustomerSerializer(data = request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def UpdateProduct(request, pk):
    Customers = Customer.objects.get(custId=pk)
    serializer = CustomerSerializer(instance = Customers, data = request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def DeleteProduct(request, pk):
    Customers = Customer.objects.get(custId=pk)
    Customers.delete()
    return Response("Customer Berhasil Di Hapus!")

@api_view(['GET'])
def CountProduct(request):
    Customer_count = Customer.objects.count()
    data = {'Customer_count': Customer_count}
    return Response(data)