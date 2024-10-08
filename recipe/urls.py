from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet,FavoriteRecipeViewSet, ReviewViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet) 
router.register(r'favorites', FavoriteRecipeViewSet, basename='favorite-recipe')
router.register(r'recipes/(?P<recipe_pk>\d+)/reviews', ReviewViewSet, basename='review')

urlpatterns = [
     path('api/', include(router.urls)),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/recipes/<int:pk>/schedule/', RecipeViewSet.as_view({'post':'schedule'}), name='recipe-schedule'),

]
urlpatterns+=router.urls