from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home_page, name='home'),
    path('create/', views.create_page, name='create')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
