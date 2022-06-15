from . import views
from django.urls import path, include

from .views import PropertyViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'property', PropertyViewSet)

urlpatterns = [
    path('', views.PropertyView.as_view()),
    path("<slug:slug>/", views.PropertyDetailView.as_view(), name="property_detail"),
    path('property/<slug:cat_slug>/', views.PropertyCategory.as_view(), name="property_category"),
    path('api/', include(router.urls)),
]
