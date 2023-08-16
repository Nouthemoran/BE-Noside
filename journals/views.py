from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializer import JournalSerializer 
from .models import Journal

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