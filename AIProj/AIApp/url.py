from django.conf.urls import *
from django.views.generic import TemplateView
from AIApp.views import *

urlpatterns = [url(r'^hello/', hello), url(r'upload/', TemplateView.as_view(template_name = 'profile.html')), url(r'saved/', SaveProfile, name = 'saved'),]
