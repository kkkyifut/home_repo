from django.urls import path
from .views import index, other_page, profile
from .views import BBLoginView, BBLogoutView
from .views import ChangeUserInfoForm, BBPasswordChangeView
from .views import RegisterUserView, RegisterDoneView
from .views import user_activate

app_name = "main"
urlpatterns = [
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
    path('accounts/profile/change', ChangeUserInfoForm.as_view(), 
        name='profile_change'),
    path('', index, name='index'),
]