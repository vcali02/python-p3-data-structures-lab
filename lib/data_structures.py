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
#1
def get_names(spicy_foods):
    spicy_foods_names = [spicy_foods[index]["name"] for index in range(3)]
    return spicy_foods_names

#print(get_names(spicy_foods))





#2
def get_spiciest_foods(spicy_foods):
    spicy_foods_spice = [spicy_foods[index] for index in range(3) if spicy_foods[index]["heat_level"] > 5]
    return spicy_foods_spice

#print(get_spiciest_foods(spicy_foods))




#3
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"]* "🌶"}')
#print_spicy_foods(spicy_foods)
    



#4
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food




#5
def print_spiciest_foods(spicy_foods):
    #create variable that filters the spiciest foods
    spiciest_foods = get_spiciest_foods(spicy_foods)
    #pass as argument the FILTERED spicy foods
    print_spicy_foods(spiciest_foods)

#don't forget to call the function
#print_spiciest_foods(spicy_foods)







#6
def get_average_heat_level(spicy_foods):
    #create baseline outside of loop
    total = 0
    #enter the loop
    #grab EACH element of the array (each food item in the list)
    for each_food in spicy_foods:
        #grab the total and for each food item, grab the heat level (a number)
        #and add it to the baseline number
        total += each_food.get("heat_level")
        #you will follow the loop instructions until there is nothing else to apply the instructions to
        #in this case, the 3 elements in the list
    #once done with the loop, will pop out the result sand move on to the next set of instructions
    #here, declare a variable and do the average math!!!! straight forward
    #len() grabs the LENGTH of the list    
    avrg = total/len(spicy_foods)
    #return the variable bc thats what you want to be as your end result
    return avrg 
#don't forget to call the function and can print to see the results        
#print(get_average_heat_level(spicy_foods))
            




#7
#the new spicy food dictionary was provided
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods



#Define a function create_spicy_food() 
#that takes a list of spicy_foods 
#and a new spicy_food and 
#returns the original list 
#with the new spicy_food added.