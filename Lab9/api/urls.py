from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import api.views
urlpatterns = [
    path("api/companies/", views.CompanyViewSet.as_view()),
    path("api/companies/<int:id>/", views.CompanyDetailSet, name="CompanyDetailSet"),
    path("api/companies/<int:id>/vacancies", CompanyVacancyViewSet.as_view()),
    path("api/vacancies/", VacancyViewSet.as_view()),
    path("api/vacancies/<int:id>", VacancyDetailSet, name="VacancyDetailSet"),
]