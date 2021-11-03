from rest_framework.routers import SimpleRouter

from prodil.record.api.views import CategoryViewSet, ResourceUpdateViewSet, ResourceViewSet

router = SimpleRouter()
router.register("resources/files", ResourceUpdateViewSet, basename="file")
router.register("resources", ResourceViewSet, basename="resource")
router.register("categories", CategoryViewSet, basename="category")
