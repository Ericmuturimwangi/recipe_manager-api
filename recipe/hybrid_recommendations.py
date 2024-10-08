from .content_based import content_based_reccomendations
from .collaborative_filtering import collaborative_reccomendations
from .models import FavoriteRecipe

def hybrid_recommendations(user):
    favorite_recipes_ids = FavoriteRecipe.objects.filter(user=user).values_list('recipe_id', flat=True)

    content_recs = content_based_reccomendations(favorite_recipes_ids)

    collab_recs = collaborative_reccomendations(user)

    combined_recs = content_recs.union(collab_recs).distinct()

    return combined_recs

