from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup, profile

app_name = "users"

urlpatterns = [
    path('account/signup/', signup, name='signup'),
    path('account/login/', auth_views.LoginView.as_view(), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(
        template_name="registration/logout.html"), name='logout'),
    path('account/profile/', profile, name='profile'),
]
