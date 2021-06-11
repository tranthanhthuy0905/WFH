from django.urls import path
from accountTracking.api.views import (registration_view)

# Compulsory once extending the urls.py
app_name ="account"

urlpatterns = [
    path('', registration_view, name="register"),
]
