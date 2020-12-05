"""Hass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.User import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/',views.Login),
    path('logout/',views.Logout),
    path('info/',views.info),
    path('tran_tem/',views.trans_temporary),
    path('Tem_decisions/',views.Tem_decision),
    path('refuse/',views.Refused),
    path('De_Formal/',views.Decision_Formal),
    path('tran_Formal/',views.tran_Formal),
    path('For_decisions/',views.For_decision),
    path('For_refuse/',views.For_refuse),
] + static(settings.MEDIA_URL,document=settings.MEDIA_ROOT)

