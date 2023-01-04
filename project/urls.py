"""project URL Configuration

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
from django.views.generic import TemplateView
from ejemplo.views import FamiliarList, FamiliarDetalle, FamiliarCrear, FamiliarBorrar, FamiliarActualizar
from proyecto_final.views import index, PostList, PostCrear

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('success_updated_message/', TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
    path('proyecto_final/', index, name="pag_index"),
    path('proyecto_final/listar/', PostList.as_view(), name="pag_listar"),
    path('proyecto_final/crear/', PostCrear.as_view(), name="pag_crear"),
]
