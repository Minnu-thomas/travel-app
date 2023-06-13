from . import views
from django.urls import path

urlpatterns = [
    path('register',views.register_fn,name='register_fn'),
    path('login',views.login_fn,name='login_fn'),
    path('logout', views.logout_fn, name='logout_fn')
]
