from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('guestnotes/', views.GuestnoteList2.as_view()),
    path('guestnotes/<int:pk>/', views.guestnote_detail),

    path('openapi', get_schema_view(
          title="Your Project",
          description="API for all things …",
          version="1.0.0"
          ), name='openapi-schema'),
    path('swagger-ui', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ))
]

# with this line, django will aknowledge the url patter variations,
# adding them to the openapi docs
# urlpatterns = format_suffix_patterns(urlpatterns)
