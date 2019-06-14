from django.urls import path,include
from rest_framework.routers import DefaultRouter

from hotelrecipe import views


router = DefaultRouter()

router.register('tag',views.TagViewSet)
router.register('ingredients',views.IngredientViewSet)
router.register('recipes',views.RecipeViewSet)

app_name = 'hotelrecipe'

urlpatterns = [
    path('',include(router.urls))
]
