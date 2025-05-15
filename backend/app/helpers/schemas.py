from pydantic import BaseModel, ConfigDict
from datetime import datetime
from uuid import UUID


class RecipeOut(BaseModel):
    recipe_id: UUID
    title: str
    description: str
    difficulty: str
    instructions: str
    image: str

    model_config = ConfigDict(from_attributes=True)


class RecipesOut(BaseModel):
    recipes: list[RecipeOut]

    model_config = ConfigDict(from_attributes=True)


class UserOut(BaseModel):
    user_id: UUID
    username: str

    model_config = ConfigDict(from_attributes=True)


class IngredientOut(BaseModel):
    ingredient_id: UUID
    name: str
    category: str

    model_config = ConfigDict(from_attributes=True)


class IngredientsOut(BaseModel):
    ingredients: list[IngredientOut]

    model_config = ConfigDict(from_attributes=True)


class FavoriteOut(BaseModel):
    favorite_id: UUID
    user_id: UUID
    recipe_id: UUID

    model_config = ConfigDict(from_attributes=True)


class FavoritesOut(BaseModel):
    favorites: list[FavoriteOut]

    model_config = ConfigDict(from_attributes=True)


class RecipeIngredientOut(BaseModel):
    ri_id: UUID
    recipe_id: UUID
    ingredient_id: UUID

    model_config = ConfigDict(from_attributes=True)
