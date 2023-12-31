"""
URL configuration for futbol_mundial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from futbol_mundial.views import InicioListView, InicioCreateView, InicioDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('futbol/', include("control.urls")),
    path('', InicioListView.as_view(), name='inicio'),
    path('', InicioCreateView.as_view(), name='crear_noticia'),
    path('noticias/<int:pk>', InicioDetailView.as_view(), name="noticias"),
    path("perfiles/", include("perfiles.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
