from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('guestnotes/', views.GuestnoteList2.as_view()),
    path('guestnotes/<int:pk>/', views.guestnote_detail),
]

# with this line, django will aknowledge the url patter variations,
# adding them to the openapi docs
# urlpatterns = format_suffix_patterns(urlpatterns)
