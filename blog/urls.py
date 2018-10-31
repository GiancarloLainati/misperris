from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rescatados/$', views.rescatado_list, name='rescatado_list'),
    url(r'^rescatados/(?P<pk>[0-9]+)/$', views.rescatado_detail,   
      name='rescatado_detail'), 
    url(r'^rescatados/new/$', views.rescatado_new, name='rescatado_new'),
    url(r'^rescatados/(?P<pk>[0-9]+)/edit/$', views.rescatado_edit, name='rescatado_edit'),
    url(r'^rescatados/(?P<pk>[0-9]+)/delete/$', views.rescatado_delete, name='rescatado_delete'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', auth_views.LoginView, name='login'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
