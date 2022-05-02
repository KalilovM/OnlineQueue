from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('', views.TalonListView.as_view(), name='talon_changelist'),
    path('add/', views.TalonCreateView.as_view(), name='talon_add'),
    path('<int:pk>/', views.TalonUpdateView.as_view(), name='talon_change'),
    path('ajax/load-cities/', views.load_filial, name='ajax_load_filials'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]