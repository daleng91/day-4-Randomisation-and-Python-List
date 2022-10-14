import random

# random_int = random.randint(0,5)
# print(random_int)
# random_float = random.random() + random.randint(0,4)
# print(random_float)
#How to create a random decimal number between 0 and 5

# random_num = random.randint(0,1)

# if random_num == 0:
#   print("Heads")
# else:
#   print("Tails")

# people_name = input("Give me everybody's name, seperated by a comma.")
# list_of_name = people_name.split(", ")
# print (list_of_name)
# num_of_items = len(list_of_name) - 1

# print(num_of_items)
# random_no = random.randint(0,num_of_items)
# print(f"{list_of_name[random_no]} is going to buy the meal today")

#my_friends = ['Dale', 'Tommy','Shane','Ping','Roshan','Winston']
# print(my_friends)
# for i in range(5):
#   print(random.choice(my_friends))

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = (fruits,vegetables)

# print(dirty_dozen)

# print(dirty_dozen[1][1])

#Day 4.3 Treasure map
row1 = ["@","@","@"]
row2 = ["@","@","@"]
row3 = ["@","@","@"]

matrix = (row1,row2,row3)
print(f"{row1}\n{row2}\n{row3}")

location = input("Please choose your choice with location (column,row): ")
location_num = int(location)
if location_num > 33:
  print("Your number is out of range, please try again!")
else:
  #location_num = str(location)
  col = int(location[0]) - 1
  row = int(location[1]) - 1
  matrix[col][row] = "X"
  print(f"{row1}\n{row2}\n{row3}")

