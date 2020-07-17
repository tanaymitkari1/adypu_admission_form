from django.urls import path
from .views import *

urlpatterns = [
    path('', input_form, name="pdf_form"),
]
