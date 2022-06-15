from . import views
from django.urls import path

urlpatterns = [
    path('', views.AgentView.as_view()),
    path("<slug:slug>/", views.AgentDetailView.as_view(), name="agent_detail"),
]