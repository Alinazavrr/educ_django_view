from django.urls import include, path
from rest_framework import routers

from api.views import HomesApi

app_name = 'api'

router = routers.DefaultRouter()
router.register('homes', HomesApi)

urlpatterns = [
    path('', include(router.urls))
]
