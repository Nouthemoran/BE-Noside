from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializer import ConferenceSerializer 
from .models import Conference

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
