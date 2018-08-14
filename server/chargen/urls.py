from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('race/', views.RaceViewSet.as_view({'get': 'list'})),
    path('class/', views.ClassViewSet.as_view({'get': 'list'})),
]
