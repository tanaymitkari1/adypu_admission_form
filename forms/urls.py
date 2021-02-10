from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', input_form, name="pdf_form"),
    path('get_data/', export_users_csv, name="data_export"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
