from . import views
from django.urls import path

urlpatterns = [
    path('',views.travel_fn,name='travel_fn')
]
