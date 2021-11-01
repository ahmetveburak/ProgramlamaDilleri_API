from rest_framework.routers import SimpleRouter

from prodil.record.api.views import CategoryViewSet, ResourceUpdateViewSet, ResourceViewSet

router = SimpleRouter()
router.register("resources/file", ResourceUpdateViewSet, basename="file")
router.register("resources", ResourceViewSet, basename="resource")
router.register("category", CategoryViewSet, basename="category")
