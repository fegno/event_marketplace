from rest_framework.routers import SimpleRouter
from apps.cms.apis import views


router = SimpleRouter()

router.register(r'assistcategory', views.AssistCategoryViewSet)


urlpatterns = router.urls
