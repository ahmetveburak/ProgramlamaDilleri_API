from rest_framework.routers import SimpleRouter

from prodil.record.api.views import ResourceViewSet

router = SimpleRouter()
router.register("resources", ResourceViewSet, basename="resource")
