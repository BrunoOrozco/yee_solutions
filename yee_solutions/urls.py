from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, url


from users import views as users_views
from crm import views as crm_views
from objetivos import views as objetivos_views
from ventas import views as ventas_views
from catalogo import views as catalogo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', users_views.login_view, name="login"),
    path('kpi/', crm_views.metrics, name="kpi"),
    path('dashboard/', ventas_views.dashboard, name="dashboard"),
    path('dashboard/ventas', ventas_views.dashboard_ventas, name="dashboard_ventas"),
    path('dashboard/<str:cliente>/', objetivos_views.UserDetailView.as_view() , name="dashboard_avances"),    
    path('logout/', users_views.logout_view, name="logout"),

    path('registro-exitoso/', crm_views.registro_exitoso, name="registro_exitoso"),

    path('crm/',                    crm_views.crm_main,             name="crm"),
    path('crm/crear-prospecto/test/', crm_views.crm_direccionProspecto, name="direccion"),
    path('crm/crear-prospecto/',     crm_views.crm_crearProspecto,   name="prospecto__crear_prospecto"),
    path('crm/crear-prospecto/crear-contacto',      crm_views.crm_crearContacto,    name="prospecto__crear_contacto"),
    path('crm/crear-contacto/crear-contacto/clasificacion', crm_views.crm_llamada_visita, name="prospecto__clasificacion"),
    path('crm/crear-prospecto/crear-contacto/clasificacion/registrar-llamada',   crm_views.crm_registrarLlamada, name="prospsecto__registrar_llamada"),
    path('crm/crear-prospecto/crear-contacto/clasificacion/registrar-visita',    crm_views.crm_registrarVisita,  name="prospecto__registrar_visita"),

    path('crm/crear-contacto', crm_views.Contacto_crearContacto, name="contacto__crear_contaccto"),
    path('crm/crear-contacto/clasificacion', crm_views.crm_contacto_clasificacion, name="contacto__clasificacion"),
    path('crm/crear-contacto/clasificacion/registrar-llamada', crm_views.Contacto_registrar_llamada, name="contacto__registrar_llamada" ),
    path('crm/crear-contacto/clasificacion/registrar-visita', crm_views.Contacto_registrar_visita, name="contacto__registrar_visita"),
    
    path('crm/registrar-llamada', crm_views.registrar_llamada, name="registrar_llamada"),
    path('crm/registrar-visita', crm_views.registrar_visita, name="registrar_visita"),

    path('disponibilidad/', catalogo_views.disponibilidad, name="disponibilidad"),
    path('disponibilidad-publica/', catalogo_views.disponibilidad_publica, name="disponibilidad_publica"),

    path('agenda/', crm_views.agenda, name="agenda"),

    path('crm/<str:nombre_comercial>/', crm_views.UserDetailView.as_view() , name="contact"),    

#
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



handler404 = users_views.Error404View.as_view()

handler500 = users_views.Error500View.as_error_view()