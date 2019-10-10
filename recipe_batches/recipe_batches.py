#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    ingredients_copy = ingredients.copy()
    batches = 0
    while True:
        for recipe_ingredients in recipe.keys():
            try:
                if ingredients_copy[recipe_ingredients] - recipe[recipe_ingredients] < 0:
                    return batches
                else:
                    ingredients_copy[recipe_ingredients] -= recipe[recipe_ingredients]
            except KeyError:
                return batches

        batches += 1


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 1000, 'butter': 350, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
