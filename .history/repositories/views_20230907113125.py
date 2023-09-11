from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializer import RepositorySerializer 
from .models import Repository
from rest_framework import status
from django.http import HttpResponse
import openpyxl
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes

@api_view(['GET'])
@permission_classes([isAuth])
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
@parser_classes([MultiPartParser])
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

@api_view(['GET'])
def search_view(request):
    repoName = request.query_params.get('repoName', '')
    repoId = request.query_params.get('repoId', '')
    address = request.query_params.get('address', '')
    
    # Lakukan pencarian berdasarkan nama konferensi
    if repoName:
        Repositories = Repository.objects.filter(repoName__icontains=repoName)
    elif repoId:
        Repositories = Repository.objects.filter(repoId__icontains=repoId)
    elif address:
        Repositories = Repository.objects.filter(address__icontains=address)
    else:
        return Response({'message': 'repository not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = RepositorySerializer(Repositories, many=True)
    return Response(serializer.data)

def download_excel(request):
    repositories = Repository.objects.all()

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append(['Repository Id', 'Repository Name', 'Address', 'Detail Repository', 'Repository Images'])

    for repository in repositories:
        worksheet.append([repository.repoId, repository.repoName, repository.address, repository.detailRepo, repository.repoImages])

    file_name = 'repositories.xlsx'

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    workbook.save(response)

    return response

@api_view(['GET'])
def sort_repo(request):
    if request.method == 'GET':
        # Ambil nilai 'ordering' dari parameter query
        ordering = request.query_params.get('ordering', None)

        # Tentukan pengurutan default jika 'ordering' tidak ada atau tidak valid
        if ordering not in ['createdAt', '-createdAt']:
            ordering = '-createdAt'  # Pengurutan berdasarkan terbaru (default)

        # Terapkan pengurutan pada queryset
        repositories = Repository.objects.all().order_by(ordering)
        serializer = RepositorySerializer(repositories, many=True)
        return Response(serializer.data)