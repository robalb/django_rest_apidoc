from django.urls import path
from snippets import views

urlpatterns = [
    path('guestnotes/', views.guestnote_list),
    path('guestnotes/<int:pk>/', views.guestnote_detail),
]
