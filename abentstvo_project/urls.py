from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from contacts.views import contacts_views
from homes.views import list_views, detail_view

from abentstvo_project import settings
from search.views import search_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homes.urls', namespace='homes')),
    path('search/', include('search.urls', namespace='search')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
    path('api/', include('api.urls', namespace='api'))
]

if settings.DEBUG is True:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)