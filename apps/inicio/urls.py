
from .views import first_view
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
  
    path('primeravista', first_view, name="first_view"),
    path('', LoginView.as_view(template_name="base.html"),name="login"),
    path('cerrar', LogoutView.as_view(),name="logout"),
]