from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

swagger_urls = [path("backend/api/", include("starwars.people.urls"))]

urls = [
    path(
        "schema/",
        SpectacularAPIView.as_view(urlconf=swagger_urls),
        name="schema",
    ),
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
