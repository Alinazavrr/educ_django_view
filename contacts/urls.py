from django.urls import path

from contacts.views import contacts_views

app_name = 'contacts'
urlpatterns = [
    path('', contacts_views, name='main')
]

