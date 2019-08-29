
from rest_framework.routers import DefaultRouter
from generates.api.views import GenerateViewSet

router = DefaultRouter()
router.register(r'', GenerateViewSet, base_name='generates')
urlpatterns = router.urls

# from django.urls import path
# from .views import (GenerateListView, GenerateDetailView,
#                     GenerateCreateView, GenerateUpdateView, GenerateDeleteView)


# urlpatterns = [
#     path('', GenerateListView.as_view()),
#     path('create/', GenerateCreateView.as_view()),
#     path('<pk>', GenerateDetailView.as_view()),
#     path('<pk>/update/', GenerateUpdateView.as_view()),
#     path('<pk>/delete/', GenerateDeleteView.as_view())

# ]
