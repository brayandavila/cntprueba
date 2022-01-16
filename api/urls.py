from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pacientes', views.ordenar, name='pacientes'),
    path('pacientes/ordenado', views.ordenarpri, name='ordenado'),
    path('pacientes/crear', views.crear, name='crear'),
    path('pacientes/actualiza/<int:id>', views.actualizar, name='actualizar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)