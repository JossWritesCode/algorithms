#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batch_counter = 0

    while True:
        for item in recipe:
            if item not in ingredients:
                return batch_counter
            if recipe[item] > ingredients[item]:
                return batch_counter
            else:
                ingredients[item] -= recipe[item]

        batch_counter += 1


print(recipe_batches(
    {'milk': 100, 'butter': 50, 'flour': 5},
    {'milk': 132, 'butter': 48, 'flour': 51}
), "should return 0")


print(recipe_batches(
    {'milk': 100, 'butter': 50, 'flour': 5},
    {'milk': 200, 'butter': 100, 'flour': 51}
), "should return 2")


if __name__ == '__main__':
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
