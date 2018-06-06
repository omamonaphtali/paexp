from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'web'


urlpatterns = [
    url(r'^$', views.index_view, name='home'),
    url(r'^profile/', views.about_view, name='profile'),
    url(r'^services/', views.services_view, name='services'),
    url(r'^rental/', views.rental_view, name='rental'),
    url(r'^gallery/', views.gallery_view, name='gallery'),
    url(r'^contact/', views.contact_view, name='contacts'),
    url(r'^blog/', views.blog_view, name='blog'),
    url(r'^topography/', views.topography_view, name='topography'),
    url(r'^projects/', views.projects_view, name='projects'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
