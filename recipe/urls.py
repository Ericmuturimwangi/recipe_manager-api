from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
     path('api/', include(router.urls)),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/', TokenRefreshView.as_view(), name='token_refresh'),

]
