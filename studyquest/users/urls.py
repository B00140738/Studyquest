from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit-profile"),
]
