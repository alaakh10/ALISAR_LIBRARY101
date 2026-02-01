from django.urls import path
from django.views.generic import TemplateView  
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education_books, name='education_books'),
    path('novels/', views.novels_books, name='novels_books'),
    path('self-development/', views.self_development_books, name='self_development_books'),
    path('history/', views.history_books, name='history_books'),
    path('translated/', views.translated_books, name='translated_books'), 
    path('religious-books/', views.religious_books, name='religious_books'),
    path('secret/', TemplateView.as_view(template_name='secret_admin.html'), name='secret_admin'),
    path('search/', views.search_books, name='search'),
]