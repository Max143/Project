from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Branches
from .serializers import BranchesSerializer
from rest_framework import filters
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination  



def testing(request):
    return render(request, 'bank/test.html')


class BankDetailView(viewsets.ModelViewSet):
    queryset = Branches.objects.all().order_by('ifsc')
    serializer_class = BranchesSerializer
    filter_backends = [filters.SearchFilter, OrderingFilter]
    # Partial Search with the field in branch
    search_fields = ['^branch']
    # Ordering Filter field by ifsc in ascending order
    ordering_fields = ['ifsc']



class BankBranchView(viewsets.ModelViewSet):
    queryset = Branches.objects.all().order_by('ifsc')
    serializer_class = BranchesSerializer
    filter_backends = [filters.SearchFilter, OrderingFilter]
    # Full Matched Search with the field in branch
    search_fields = ['=branch']
    ordering_fields = ['ifsc']



