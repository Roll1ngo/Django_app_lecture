from django.urls import path, include
from . import views

app_name = "app_photo"

urlpatterns = [
    path('', views.index, name='home'),
    path('images/', views.pictures, name='pictures'),
    path('upload/', views.upload, name='upload'),
    path('images/edit/<int:pic_id>', views.edit, name='edit'),
    path('images/remove/<int:pic_id>', views.remove, name='remove')
]
