from rest_framework.serializers import ModelSerializer

from .models import Company, Vacancy

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'name', 'description', 'city', 'address'
        )
class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'name', 'description', 'salary', 'company'
        )