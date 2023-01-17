from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'rooms', RoomlViewset)
router.register(r'messages', MessageViewset)
router.register(r'writers', WriterViewset)
router.register(r'users', UserViewset)


urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]