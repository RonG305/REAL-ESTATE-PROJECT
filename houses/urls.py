from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Houses, name='index'),
    path('add_house/', views.add_house, name='add_house'),
    path('update_house/<str:pk>/', views.update_house, name='update_house'),
    path('delete_house/<str:pk>/', views.delete_house, name='delete_house')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)