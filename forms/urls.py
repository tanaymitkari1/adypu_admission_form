from django.urls import path
from .views import *

urlpatterns = [
    path('', input_form, name="pdf_form"),
    path('get_data/', export_users_csv, name="data_export"),
]
