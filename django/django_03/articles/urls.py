from django.contrib import admin
from django.urls import path
from . import views
import articles

app_name = 'articles'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('update/<int:pk>', views.update, name="update")
]