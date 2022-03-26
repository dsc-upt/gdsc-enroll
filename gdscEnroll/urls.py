from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('', include('backend.urls')),
    path('admin/', admin.site.urls),
    path("api-auth_rest/",
         include("rest_framework.urls", namespace="rest_framework")),

    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
    path('auth/', include('auth_rest.urls')),
]
