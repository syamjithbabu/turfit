from . import views
from django.urls import path

app_name = 'website'

urlpatterns = [
    path('',views.login,name="login"),
    path('sign-up',views.sign_up,name="sign_up")
]