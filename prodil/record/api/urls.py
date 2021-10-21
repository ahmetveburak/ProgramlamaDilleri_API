from rest_framework.routers import SimpleRouter

from prodil.record.api.views import CategoryViewSet, ResourceViewSet

router = SimpleRouter()
router.register("resources", ResourceViewSet, basename="resource")
router.register("category", CategoryViewSet, basename="category")
