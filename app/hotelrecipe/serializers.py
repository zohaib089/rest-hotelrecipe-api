from rest_framework import serializers
from core.models import Tag, Ingredient,Recipe


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag Objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ("id",)


class IngredientSerializer(serializers.ModelSerializer):
    """Searilizer for ingredients objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ("id",)

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe"""
    ingredients = serializers.PrimaryKeyRelatedField(many=True,queryset=Ingredient.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True,queryset=Tag.objects.all())
    class Meta:
        model = Recipe
        fields =('id','title','ingredients','tags','time_minutes','price','link')
        read_only_fields=('id',)

class RecipeDetailSerializer(RecipeSerializer):
    """serializer a recipe Detail"""
    ingredients = IngredientSerializer(many=True,read_only=True)
    tags = TagSerializer(many=True,read_only=True)

