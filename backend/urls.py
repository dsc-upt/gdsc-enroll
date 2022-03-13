from django.urls import include, path
from backend.Views.rest_views import UserViewSet, GroupViewSet
from rest_framework import routers
from backend.Views.new_ticket import new_ticket


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("/new-ticket/", include(new_ticket)),
]
