from django.urls import include, path
from backend.Views.rest_views import UserViewSet, GroupViewSet
from rest_framework import routers
from backend.Views.new_ticket import new_ticket
from backend.Views.dashboard_view import dashboard


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)

urlpatterns = [
    path("", dashboard),
    path("/", include(router.urls)),
    path("new-ticket/", new_ticket),
]
