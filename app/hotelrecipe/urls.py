from django.urls import path,include
from rest_framework.routers import DefaultRouter

from hotelrecipe import views


router = DefaultRouter()

router.register('tag',views.TagViewSet)

app_name = 'hotelrecipe'

urlpattern = [
    path('',include(router.urls))
]
