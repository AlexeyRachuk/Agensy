from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogView.as_view()),
    path("<slug:slug>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path('blog/<slug:cat_slug>/', views.BlogCategory.as_view(), name="category")
]
