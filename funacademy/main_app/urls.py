from django.urls import path
from .views import Home
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup')
    # Other URL patterns...
]