# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students(students):
    first_student = students[1]
    last_student = students[-1]
    return(f"First student variable contains: {first_student} \n Last student variable contains: {last_student}")

# Call the function and print the result
students = ['Firstington Firstson','Secundos Secondson','Thirinias Thridson','Quirinious Quartetus']
print('Exercise 1: \n', manage_students(students))


# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.
food= ('pizza','apple','bread','cod')
def combine_foods(food):
    meal="" 
    for element in food:
        meal +=element +" "
    return meal

# Call the function and print the result
print('Exercise 2:', combine_foods(food))

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods(food):
    x=slice(-2,0,-1)
    return food[x]

# Call the function and print the result
print('Exercise 3:', slice_foods(food))

# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”
home_town={
    'city':'Cordoba',
    'state' : 'Andalucia',
    'population' : '10k',
}
def hometown_info(home_town):
    home_town_message = (f"I was born in {home_town.get('city')}, {home_town.get('state')} - population of {home_town.get('population')}")
    return home_town_message

# Call the function and print the result
print('Exercise 4:', hometown_info(home_town))

# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items(home_town):
    home_town_items = []
    for key, value in home_town.items():
        home_town_items.append(f"<{key}> = <{value}>")
    return home_town_items

# Call the function and print the result
print('Exercise 5:', list_home_town_items(home_town))

