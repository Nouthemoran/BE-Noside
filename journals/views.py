from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializer import JournalSerializer 
from .models import Journal
from rest_framework import status
from django.http import HttpResponse
import openpyxl

@api_view(['GET'])
def ShowAll(request):
    Journals = Journal.objects.all()
    serializer = JournalSerializer(Journals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request, pk):
    Journals = Journal.objects.get(jurnalId=pk)
    serializer = JournalSerializer(Journals, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    serializer = JournalSerializer(data = request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def UpdateProduct(request, pk):
    Journals = Journal.objects.get(jurnalId=pk)
    serializer = JournalSerializer(instance = Journals, data = request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def DeleteProduct(request, pk):
    Journals = Journal.objects.get(jurnalId=pk)
    Journals.delete()
    return Response("Journal Berhasil Di Hapus!")

@api_view(['GET'])
def CountProduct(request):
    Journal_count = Journal.objects.count()
    data = {'Journal_count': Journal_count}
    return Response(data)

@api_view(['GET'])
def search_view(request):
    jurnalName = request.query_params.get('jurnalName', '')
    jurnalId = request.query_params.get('jurnalId', '')
    
    # Lakukan pencarian berdasarkan nama konferensi
    if jurnalName:
        Journals = Journal.objects.filter(jurnalName__icontains=jurnalName)
    elif jurnalId:
        Journals = Journal.objects.filter(jurnalId__icontains=jurnalId)
    else:
        return Response({'message': 'journal not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = JournalSerializer(Journals, many=True)
    return Response(serializer.data)

def download_excel(request):
    journals = Journal.objects.all()

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append(['Journal Id', 'Journal Name', 'Email', 'Phone Number', 'Status'])

    for journal in journals:
        worksheet.append([journal.jurnalId, journal.jurnalName, journal.alias, journal.detailJurnal, journal.jurnalImages])

    file_name = 'journals.xlsx'

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    workbook.save(response)

    return response