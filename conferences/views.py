from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializer import ConferenceSerializer 
from .models import Conference
from rest_framework import status
import openpyxl
from django.http import HttpResponse



@api_view(['GET'])
def ShowAll(request):
    Conferences = Conference.objects.all()
    serializer = ConferenceSerializer(Conferences, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request, pk):
    Conferences = Conference.objects.get(confId=pk)
    serializer = ConferenceSerializer(Conferences, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    serializer = ConferenceSerializer(data = request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def UpdateProduct(request, pk):
    Conferences = Conference.objects.get(confId=pk)
    serializer = ConferenceSerializer(instance = Conferences, data = request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def DeleteProduct(request, pk):
    Conferences = Conference.objects.get(confId=pk)
    Conferences.delete()
    return Response("Conference Berhasil Di Hapus!")

@api_view(['GET'])
def CountProduct(request):
    Conference_count = Conference.objects.count()
    data = {'Conference_count': Conference_count}
    return Response(data)

@api_view(['GET'])
def search_view(request):
    conf_name = request.query_params.get('confName', '')
    conf_id = request.query_params.get('confId', '')
    
    
    # Lakukan pencarian berdasarkan nama konferensi
    if conf_name:
        conferences = Conference.objects.filter(confName__icontains=conf_name)
    if conf_id:
        conferences = Conference.objects.filter(confId__icontains=conf_id)
    else:
        return Response({'message': 'conference not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ConferenceSerializer(conferences, many=True)
    return Response(serializer.data)

def download_excel(request):
    conferences = Conference.objects.all()

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append(['Conference Id', 'Conference Name', 'Detail', 'Images'])

    for conference in conferences:
        worksheet.append([conference.confId, conference.confName, conference.detailConf, conference.confImages])

    file_name = 'conferences.xlsx'

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    workbook.save(response)

    return response
