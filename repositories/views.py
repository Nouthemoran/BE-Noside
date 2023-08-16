from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializer import RepositorySerializer 
from .models import Repository
from rest_framework.views import APIView

@api_view(['GET'])
def ShowAll(request):
    Repositories = Repository.objects.all()
    serializer = RepositorySerializer(Repositories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request, pk):
    Repositories = Repository.objects.get(repoId=pk)
    serializer = RepositorySerializer(Repositories, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    serializer = RepositorySerializer(data = request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def UpdateProduct(request, pk):
    Repositories = Repository.objects.get(repoId=pk)
    serializer = RepositorySerializer(instance = Repositories, data = request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def DeleteProduct(request, pk):
    Repositories = Repository.objects.get(repoId=pk)
    Repositories.delete()
    return Response("Repository Berhasil Di Hapus!")

@api_view(['GET'])
def CountProduct(request):
    Repository_count = Repository.objects.count()
    data = {'Repository_count': Repository_count}
    return Response(data)