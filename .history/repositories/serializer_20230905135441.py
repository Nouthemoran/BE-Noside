from rest_framework import serializers
from .models import Repository

class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields  = ['repoId', 'repoName', 'address', 'detailRepo', 'repoImages','background','urlsRepo']