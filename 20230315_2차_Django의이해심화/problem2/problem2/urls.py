
from django.urls import path, include

urlpatterns = [
    path('cal/', include('calculators.urls')),
]
