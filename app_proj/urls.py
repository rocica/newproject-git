from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/app_proj', ProjectViewSet, 'app_proj')

urlpatterns = router.urls
