from django.conf import settings
from django.conf.urls.defaults import patterns
from django.views.generic import TemplateView
from staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    (r'^/?$', TemplateView.as_view(template_name='hello.html')),
)

urlpatterns += staticfiles_urlpatterns()
