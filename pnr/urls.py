from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("pnr/", views.PNRList.as_view()),
    path("pnr/<str:pnr_number>/", views.PNRDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)