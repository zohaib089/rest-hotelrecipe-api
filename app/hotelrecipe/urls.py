from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import TagViewSet,IngredientViewSet


router = DefaultRouter()

router.register('tag',TagViewSet)
router.register('ingredient',IngredientViewSet)

app_name = 'hotelrecipe'

urlpatterns = [
    path('',include(router.urls))
]
