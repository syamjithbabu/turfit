from . import views
from django.urls import path

app_name = 'website'

urlpatterns = [
    path('',views.login_view,name="login"),
    path('sign-up',views.sign_up,name="sign_up"),
    path('logout',views.logout_view,name="logout")
]