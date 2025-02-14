from django.urls import path
from .views import home, scan_status, scan_results


urlpatterns = [
    path('', home, name='home'),
    path('scan_status/<scan_id>/', scan_status, name='scan_status'),
    path('scan_results/', scan_results, name='scan_results'),
]
