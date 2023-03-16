
from django.urls import path, include

urlpatterns = [
    path('calculators/', include('calculators.urls')),
]
