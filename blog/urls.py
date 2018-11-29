from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from blog.quickstart.views import RescatadoViewSet

router = routers.DefaultRouter()
router.register(r'rescatados', RescatadoViewSet)

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
    url(r'^login/$', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name='blog/password_reset_form.html'), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^charcha-serviceworker(.*.js)$', views.charcha_serviceworker, name='charcha_serviceworker'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
