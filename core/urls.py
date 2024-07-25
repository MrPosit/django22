from django.contrib import admin
from django.urls import path
from app.views import home, SignUp, CustomLogoutView, CustomLoginView, profile, high_balance_accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('high_balance_accounts/', high_balance_accounts, name='high_balance_accounts'),
]

