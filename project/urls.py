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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import FamiliarList, FamiliarDetalle, FamiliarCrear, FamiliarBorrar, FamiliarActualizar
from proyecto_final.views import index, Nosotros, Config
from proyecto_final.views import PostList, PostCrear, PostActualizar, PostBorrar, PostrDetalle, UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar
from proyecto_final.views import MensajeBorrar, MensajeCrear, MensajeDetalle, MensajeListar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('success_updated_message/', TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
    path('proyecto_final/', index, name="pag_index"),
    path('proyecto_final/nosotros/', Nosotros, name="pag_nosotros"),
    path('proyecto_final/config/', Config, name="pag_config"),
    path('proyecto_final/listar/', PostList.as_view(), name="pag_listar"),
    path('proyecto_final/crear/', PostCrear.as_view(), name="pag_crear"),
    path('proyecto_final/<int:pk>/actualizar/', PostActualizar.as_view(), name="pag_actualizar"),
    path('proyecto_final/<int:pk>/borrar/', PostBorrar.as_view(), name="pag_borrar"),
    path('proyecto_final/<int:pk>/detalle/', PostrDetalle.as_view(), name="pag_detalle"),
    path('proyecto_final/signup/', UserSignUp.as_view(), name="pag_signup"),
    path('proyecto_final/login/', UserLogin.as_view(), name="pag_login"),
    path('proyecto_final/logout/', UserLogout.as_view(), name="pag_logout"),
    path('proyecto_final/avatar/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="pag_avatar_act"),
    path('proyecto_final/user/<int:pk>/actualizar/', UserActualizar.as_view(), name="pag_config_perfil"),
    path('proyecto_final/mensaje/listar/', MensajeListar.as_view(), name="pag_mensaje_listar"),
    path('proyecto_final/mensaje/<int:pk>/detalle/', MensajeDetalle.as_view(), name="pag_mensaje_detalle"),
    path('proyecto_final/mensaje/crear/', MensajeCrear.as_view(), name="pag_mensaje_crear"),
    path('proyecto_final/mensaje/<int:pk>/borrar/', MensajeBorrar.as_view(), name="pag_mensaje_borrar"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)