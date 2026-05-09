from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KPIViewSet, PerformanceReviewViewSet, GoalViewSet

router = DefaultRouter()
router.register(r'goal', GoalViewSet)
router.register(r'kpis', KPIViewSet)
router.register(r'review', PerformanceReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
