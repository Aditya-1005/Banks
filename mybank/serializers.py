from rest_framework import serializers
from .models import Banks,Branches


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ['IFSC', 'Branch', 'Address', 'City', 'District', 'State']


class BankSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True,read_only=True)
    class Meta:
        model = Banks
        fields = ['ID','Name','branches']