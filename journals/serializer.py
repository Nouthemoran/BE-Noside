from rest_framework import serializers
from .models import Journal
class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields  = ['jurnalId', 'jurnalName', 'alias', 'detailJurnal', 'jurnalImages']