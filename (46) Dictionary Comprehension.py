# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions

# dictionary = {key: expression for (key, value) in iterable}
#              {key: expression for (key, value) in iterable if condition}
#              {key: (if/else) for (key, value) in iterable}

cities_in_F = {"New York": 32, "Los Angeles": 100, "Chicago": 50, "Boston": 42}
cities_in_C = {key: round((value-32)*5/9) for key,value in cities_in_F.items()}
print(cities_in_C)


# if conditional:
weather = {"New York": "sunny", "Los Angeles": "sunny", "Chicago": "rainy", "Boston": "cloudy"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)


# if/else conditional:
cities_weather = {"New York": 32, "Los Angeles": 100, "Chicago": 50, "Boston": 42}
cities_temp = {key: ("WARM" if value >= 40 else "COLD") for key,value in cities_weather.items()}
print(cities_temp)

# using function in place of the expression:
def temp_check(value):
    if value >= 40:
        return "HOT"
    else:
        return "COLD"

cities_weather = {"New York": 32, "Los Angeles": 100, "Chicago": 50, "Boston": 42}
cities_temp = {key: temp_check(value) for key,value in cities_weather.items()}
print(cities_temp)
