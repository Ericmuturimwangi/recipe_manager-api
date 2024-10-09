from .content_based import content_based_reccomendations
from .collaborative_filtering import collaborative_reccomendations
from .models import FavoriteRecipe

def hybrid_recommendations(user):
    # having the correct recipe IDs for the current user
    favorite_recipes_ids = FavoriteRecipe.objects.filter(user=user).values_list('recipe_id', flat=True)

    # get content based recommendations based on the favorite recipe
    content_recs = content_based_reccomendations(favorite_recipes_ids)

    # collaborative filtering recs for the user.
    collab_recs = collaborative_reccomendations(user)

    combined_recs = content_recs.union(collab_recs).distinct()

    return combined_recs

