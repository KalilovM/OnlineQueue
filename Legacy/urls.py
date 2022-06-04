from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('', views.home, name='test'),
    path('add/', views.TalonCreateView.as_view(), name='talon_add'),
    path('<int:pk>/', views.TalonUpdateView.as_view(), name='talon_change'),
    path('ajax/load-cities/', views.load_filial, name='ajax_load_filials'),
    path('<pk>/delete/', views.TalonDeleteView.as_view(), name='talon_delete'),


    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('User/<int:pk>', views.UpdateUser, name='user-update')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)