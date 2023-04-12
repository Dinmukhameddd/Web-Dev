from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.http import JsonResponse

from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

class CompanyViewSet(generics.ListCreateAPIView,
                    generics.RetrieveUpdateDestroyAPIView
                    ):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
def CompanyDetailSet(request,id):
    try:
        serializer_class = CompanySerializer
        queryset = Company.objects.get(id = id)
        data = {'queryset':{
            'name': queryset.name,
            'description': queryset.description,
            'city': queryset.city,
            'address': queryset.address
        }}
    except Company.DoesNotExist:
        data = {'error': 'Company not found'}
    return render(data)
class CompanyVacancyViewSet(generics.ListCreateAPIView,
                    generics.RetrieveUpdateDestroyAPIView,
                    request,
                    id
                    ):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.filter(id = id)
class VacancyViewSet(generics.ListCreateAPIView,
                    generics.RetrieveUpdateDestroyAPIView,
                    ):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
def VacancyDetailSet(request,id):
    try:
        serializer_class = VacancySerializer
        queryset = Vacancy.objects.get(id = id)
        data = {'queryset':{
            'name': queryset.name,
            'description': queryset.description,
            'salary': queryset.salary,
            'company': queryset.company
        }}
    except Vacancy.DoesNotExist:
        data = {'error': 'Vacancy not found'}
    return render(data)

