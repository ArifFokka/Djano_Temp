from django.urls import path
from .import views
# Ami banisi nije urls.
urlpatterns = [
   path('',views.HomeView.as_view(), name='home'),
   path('about/',views.AboutView.as_view(), name='about')
]