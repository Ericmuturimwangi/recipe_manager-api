from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, FavoriteRecipeViewSet, RecipeRecommendationView
from User_Activity.views import ReviewCreateView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'recipes', RecipeViewSet) 
router.register(r'favorites', FavoriteRecipeViewSet, basename='favorite-recipe')
router.register(r'recipes/(?P<recipe_pk>\d+)/reviews', ReviewCreateView, basename='review')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/recipes/<int:pk>/schedule/', RecipeViewSet.as_view({'post': 'schedule'}), name='recipe-schedule'),
    path('api/recipes/recommendations/', RecipeRecommendationView.as_view(), name='recipe-recommendations'),
    path('api/user/profile/', UserProfileView.as_view(), name='user-profile'),
]