from rest_framework import serializers
from .models import Branches



class BranchesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Branches
        fields = ['url' ,'ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state']







