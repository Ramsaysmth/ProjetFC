"""ProjectFC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from hello.views import firstScreenSetup, phraseScreenSetup, mainScreen, delete_eleve, resultScreen, matchingWordsScreen, mainMenu, lockedMenu

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', mainMenu, name='mainMenu'),
    path('admin/', admin.site.urls, name='admin'),
    path('setupfc/', firstScreenSetup, name='firstScreenSetup'),
    path('matchingword/', matchingWordsScreen, name='matchingWordsScreen'),
    path('lockedMenu/', lockedMenu, name='lockedMenu'),
    path('setupphr/', phraseScreenSetup, name='phraseScreenSetup'),
    path('mainScreen/', mainScreen, name='mainScreen'),
    path('delete', delete_eleve, name='delete_eleve'),
    path('result/', resultScreen, name='resultScreen'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
