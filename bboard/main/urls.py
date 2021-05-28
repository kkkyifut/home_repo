from django.urls import path

from .views import (BBLoginView, BBLogoutView, BBPasswordChangeView,
                    ChangeUserInfoForm, DeleteUserView, RegisterDoneView,
                    RegisterUserView, by_rubric, index, other_page, profile,
                    user_activate)

app_name = "main"
urlpatterns = [
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('accounts/register/done/', RegisterDoneView.as_view(),
         name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/activate/<str:sign>/', user_activate, 
         name='register_activate'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change', BBPasswordChangeView.as_view(),
         name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/delete', DeleteUserView.as_view(), 
         name='profile_delete'),
    path('accounts/profile/change', ChangeUserInfoForm.as_view(), 
         name='profile_change'),
    path('', index, name='index'),
]
