from django.urls import path
from taskTracking import views

urlpatterns=[
    path('', views.report_list),
    path('<int:pk>/', views.report_detail)
]
