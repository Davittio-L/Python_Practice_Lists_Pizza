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
animal_facts = [
    ('Wolf', 'Wolves are known to be pact animals who are very social.'),
    ('Mountain Lion', 'Mountain Lions are also called Cougers or Pumas.'),
    ('Brown Bear', 'Brown Bears are brown.'),
    ('Eagle', 'Eagles have excellent vision and can spot pray from extremely far away.')
]

discussion_animal = 'Wolf'

found = False
for animal, fact in animal_facts:
    if animal == discussion_animal:
        print(f"One fun fact about {animal}: {fact}")
        found = True
        break

if not found:
    print(f"Sorry, I could not find a fact about {discussion_animal}")