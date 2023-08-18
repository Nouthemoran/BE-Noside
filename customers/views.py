from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializer import CustomerSerializer 
from .models import Customer
from rest_framework import status
from django.http import HttpResponse
import openpyxl

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

@api_view(['GET'])
def search_view(request):
    name = request.query_params.get('name', '')
    custId = request.query_params.get('custId', '')
    status = request.query_params.get('status', '')
    
    # Lakukan pencarian berdasarkan nama konferensi
    if name:
        Customers = Customer.objects.filter(name__icontains=name)
    elif custId:
        Customers = Customer.objects.filter(custId__icontains=custId)
    elif status:
        Customers = Customer.objects.filter(status__icontains=status)
    else:
        return Response({'message': 'customer not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CustomerSerializer(Customers, many=True)
    return Response(serializer.data)

def download_excel(request):
    customers = Customer.objects.all()

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append(['Customer Id', 'Customer Name', 'Email', 'Phone Number', 'Status'])

    for customer in customers:
        worksheet.append([customer.custId, customer.name, customer.email, customer.phoneNumber, customer.status])

    file_name = 'customers.xlsx'

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    workbook.save(response)

    return response