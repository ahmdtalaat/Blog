from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup, profile

app_name = "users"

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    path('profile/', profile, name='profile'),
]
