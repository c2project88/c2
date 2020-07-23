from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='auth/index.html'))

]
