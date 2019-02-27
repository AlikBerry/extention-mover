from django.urls import path
from scrapping_app.views import *

urlpatterns = [
    path('api/',DataCreate.as_view())
]
