from django.urls import include, path
from backend.Views.rest_views import UserViewSet
from rest_framework import routers
from backend.Views.new_ticket import NewTicket
from backend.Views.thank_you import thank_you


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("new-ticket/", NewTicket.as_view()),
    path("thank-you/", thank_you)
]
