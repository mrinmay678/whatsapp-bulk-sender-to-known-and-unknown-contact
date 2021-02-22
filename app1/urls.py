from django.urls import path
from .views import upload_csv_here, upload_unknown_csv_here
urlpatterns = [
    path('known/', upload_csv_here),
    path('unknown/', upload_unknown_csv_here),
]
