from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views

app_name = 'generator'
urlpatterns = [
    path('', views.index, name='index'),
    path('makepoem/', views.MakePoem, name='makepoem'),
    path('getpoempub/', views.GetPoemPub, name='getpoempub'),
    # favicon
    path('favicon.ico/', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
]