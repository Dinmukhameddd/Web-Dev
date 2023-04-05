from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import ProductViewSet, CategoryViewSet

urlpatterns = [
    path("api/products/", ProductViewSet.as_view()),
    path("api/products/<int:id>/",ProductViewSet.as_view()),
    path("api/categories/", CategoryViewSet.as_view()),
    path("api/categories/<int:id>/",CategoryViewSet.as_view()),
    path("api/categories/<int:id>/products",CategoryViewSet.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)