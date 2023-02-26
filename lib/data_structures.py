import ipdb
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
# spicy_foods is a list, inside the list are dictionaries
# with dictionaries, 
# ".get" is preferred over bracket notation in most cases 
# because it will return "None" instead of an error

# List Comprehensions => []
# map like 
# return a list of strings with the names of each spicy food
# ["Green Curry", "Buffalo Wings", "Mapo Tofu"]
def get_names(spicy_foods):
    food_names = [food.get('name') for food in spicy_foods]
    return food_names
    # OR IN ONE LINE:
    # return [food["name"] for food in spicy_foods]

# List Comprehensions => []
# filter like 
# return a list of dictionaries where the heat level > 5
# [{"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}, {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}]
def get_spiciest_foods(spicy_foods):
    # food_names = [RETURNED FOOD / LOOP / CONDITIONAL]
    food_names = [food for food in spicy_foods if food.get('heat_level') > 5]
    return food_names
    # OR IN ONE LINE:
    # return [food for food in spicy_foods if food["heat_level"] > 5]

# output to the terminal each spicy food in the following format 
# using print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        # both works
        # name = food['name']
        # cuisine = food['cuisine']
        # heat = food['heat_level'] * '🌶' 
        name = food.get('name')
        cuisine = food.get('cuisine')
        heat = food.get('heat_level') * '🌶' 
        print(f'{name} ({cuisine}) | Heat Level: {heat}')
        # OR IN ONE LINE:
        # print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

# return a single dictionary for the spicy food 
# whose cuisine matches the cuisine being passed to the method.
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # BELOW RETURNS [{}]
    # food = [food for food in spicy_foods if food.get('cuisine') == cuisine]
    # return food
    # BELOW RETURNS {}, WHICH THE TEST IS ASKING FOR !
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food
      
#output to the terminal ONLY the spicy foods that have a heat > 5, 
# in the same format: 
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food.get('heat_level') > 5:
            name = food.get('name')
            cuisine = food.get('cuisine')
            heat = food.get('heat_level') * '🌶' 
            print(f'{name} ({cuisine}) | Heat Level: {heat}')
    # OR JUST PASS IN PREV WRITTEN FUNCTIONS            
    # spiciest_foods = get_spiciest_foods(spicy_foods)
    # print_spicy_foods(spiciest_foods)

# returns an integer representing the average heat 
# level of all the spicy foods in the array.

def get_average_heat_level(spicy_foods):
    heat_level = []
    for food in spicy_foods:
        heat_level.append(food.get('heat_level'))
    return sum(heat_level) / len(spicy_foods)
    # OR
    # heat_levels = [food.get('heat_level') for food in spicy_foods]
    # return sum(heat_levels) / len(spicy_foods)
    # OR
    # sum = 0
    # for food in spicy_foods:
    #     heat_level = food.get('heat_level')
    #     sum += heat_level
    # return sum / len(spicy_foods)

# return the original list with the new spicy_food added.
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

# def get_average_heat_level(spicy_foods):
#     # WHY DOESN'T THIS WORK?
#     for food in spicy_foods:
#         heat_level = food.get('heat_level')
#     ave = sum(heat_level) / len(spicy_foods)
#     return ave
get_average_heat_level(spicy_foods)
