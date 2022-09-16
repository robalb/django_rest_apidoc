from django.urls import path
from restapi import views
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    # Rest API endpoints
    path('guestnotes/', views.GuestnoteList2.as_view()),
    path('guestnotes/<int:pk>/', views.guestnote_detail),

    # Live openapi specification yaml
    path('openapi', get_schema_view(
          title="Demoapp DRF",
          description="A simple rest api written using DRF, with the goal of testing it's introspection algoritm",
          version="1.0.0"
          ), name='openapi-schema'),
    # Swagger ui for the openapi specification
    path('swagger-ui', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name="swagger-ui"),
    # Demo app homepage
    path('', TemplateView.as_view(
        template_name='homepage.html',
        extra_context={'schema_url': 'openapi-schema', 'swagger_url': 'swagger-ui'}
    )),
]