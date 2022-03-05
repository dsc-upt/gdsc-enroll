from django.urls import include, path
from backend.Views.rest_views import UserViewSet, GroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),

]
