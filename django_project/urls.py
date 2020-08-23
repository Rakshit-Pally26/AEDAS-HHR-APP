"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from userinfo import views
from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^aedas/', include('userinfo.urls')),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^contact/', views.ContactUs, name='contact'),
    url(r'^contactinfo/', views.ContactInfo, name='contactinfo'),
    url(r'^slackmenu/', views.SlackMenu, name='slackmenu'),
    url(r'^documents/', views.document_list, name='document_list'),
    url(r'^documents_upload/', views.document_upload, name='document_upload'),
    url(r'^add_user/', views.AddUser, name='add_user'),
    url(r'^all_users/', views.AllUsers, name='all_users'),
    url(r'^add_user_form_submission/', views.add_user_form_submission, name='add_user_form_submission'),
    path('pdf_view/<int:id>/', views.Generate, name="pdf_generate"),
    path('map_view/', views.default_map, name="default_map"),
    path('drought_monitor/', views.drought_monitor, name="drought_monitor"),
    path('crop_monitor/', views.crop_monitor, name="crop_monitor"),
    path('vdri_monitor/', views.vdri_monitor, name="vdri_monitor"),
    path('qdri_monitor/', views.qdri_monitor, name="qdri_monitor"),
    path('eddi_monitor/', views.eddi_monitor, name="eddi_monitor"),
    path('esi_monitor/', views.esi_monitor, name="esi_monitor"),
    path('map_view1/', views.default_map1, name="default_map1"),
    path('map_data/', views.map_data, name="map_data"),
    path('map_nasa/', views.map_nasa, name="map_nasa"),
    path('map_nasa1/', views.map_nasa1, name="map_nasa1"),
    path('map_nasa2/', views.map_nasa2, name="map_nasa2"),
    path('map_groundwater/', views.map_groundwater, name="map_groundwater"),
    path('map_groundwater1/', views.map_groundwater1, name="map_groundwater1"),
    path('map_groundwater2/', views.map_groundwater2, name="map_groundwater2"),
    path('map_drought1/', views.map_drought1, name="map_drought1"),
    path('map_drought2/', views.map_drought2, name="map_drought2"),
    path('map_hazard/', views.map_hazard, name="map_hazard"),
    path('map_soil/', views.map_soil, name="map_soil"),
    path('map_soil1/', views.map_soil1, name="map_soil1"),
    path('map_soil2/', views.map_soil2, name="map_soil2"),
    path('map_fire1/', views.map_fire1, name="map_fire1"),
    path('map_fire2/', views.map_fire2, name="map_fire2"),
    path('map_fire3/', views.map_fire3, name="map_fire3"),
    path('map_fire4/', views.map_fire4, name="map_fire4"),
    path('map_tool/', views.map_tool, name="map_tool"),
    path('map_cmi/', views.map_cmi, name="map_cmi"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)