#Simple Practice of Lsits:
# pizza_names = ['Pepperoni', 'Hawaiian', 'Cheese',]
# for pizzas in pizza_names:
#     print(pizza_names)

# #---------------------------------------------------
# #New List
# animals = ['Wolf', 'Mountain Lion', 'Brown Bear', 'Eagle']
# for animal in animals:
#     print(animals)
#     print(f"the top preditor animals of the Rocky Mountians are {animals}")

#---------------------------------------
# animal_facts = [
#     ('Wolf', 'Wolves are known to be pact animals who are very social.'),
#     ('Mountain Lion', 'Mountain Lions are also called Cougers or Pumas.'),
#     ('Brown Bear', 'Brown Bears are brown.'),
#     ('Eagle', 'Eagles have excellent vision and can spot pray from extremely far away.')
# ]

# discussion_animal = 'Wolf'

# found = False
# for animal, fact in animal_facts:
#     if animal == discussion_animal:
#         print(f"One fun fact about {animal}: {fact}")
#         found = True
#         break

# if not found:
#     print(f"Sorry, I could not find a fact about {discussion_animal}")

# Numerical Lists
for value in range(1, 11):   # Remember that range() prints one less than final number. so if you want 1-10 your range() should be 1, 11.
    print(value)

#Prints a list of numbers 
numbers = list(range(1, 11))
print(numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)