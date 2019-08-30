from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from gen import views

urlpatterns = [
    path('gen/', views.gen_list)
]

urlpatterns = format_suffix_patterns(urlpatterns)
