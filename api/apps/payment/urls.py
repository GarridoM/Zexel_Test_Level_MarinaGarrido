from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet

router = DefaultRouter()
router.register(r'api/payments', PaymentViewSet, basename='payment')

urlpatterns = router.urls
# urlpatterns = [
#     path('', include(router.urls)),
# ]