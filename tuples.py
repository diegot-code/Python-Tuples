
#__________________________________________________________________________________________________________________
# Tuples
print("Start of Python Tuple...")

topics = ("Laws of Physics", "Taxes", "Death", "Numbers", "pi", "e") # tuples are immutable/unchangable

# print(topics)
# print(type(topics))


# list_ex = ["Stuff", "More Stuff", "Even More Stuff", "Too Much Stuff"] # example syntax difference of tuples and lists
# print(type(list_ex))


human1 = ("Gerald")

# print(type(human1))

human2 = ("George",)

# print(type(human2))

#__________________________________________________________________________________________________________________
# Access

# items in a tuple have index values\

# print(topics[0])

# print(topics[3])

# print(topics[-1])

# print(topics[-4])

#-------------------------------------------
# check if "Numbers" exists in the tuple

# if "Numbers" in topics:
#     print("Numbers be in there")


#__________________________________________________________________________________________________________________
# Unpack

(science, economics, philosophy, *math) = topics

# print(science)

# print(economics)

# print(philosophy)

# print(math)

#-------------------------------------------

sec_tuple = ("Florida", "Games", "13", "65", "124", "7")

(state, entertainment, *numbers) = sec_tuple 

# print(state)

# print(entertainment)

# print(numbers) # assigns as list
# num_list = sec_tuple[2:] # assigns as tuple


#__________________________________________________________________________________________________________________
# Update

# topics.append("Rabbit") # tuples cannot be added to

fruits = ("apple", "kiwi", "banana", "cherry", "orange", "avocado", "durian", "rasberry", "blackberry", "lemon", "lime", "watermelon")

# print(fruits)

listed_fruits = list(fruits)

# print(listed_fruits)

listed_fruits[2] = "melon"

listed_fruits.append("persimmon")

fruits = tuple(listed_fruits)

# print(fruits)

#-------------------------------------------

subjects = ("Math", "Math", "Algebra", "Geometry", "Algebra", "Trigonometry")

# print(subjects)

# subject = ("Calculus",)

# subjects += subject

# print(subjects)

# Check for duplicates
# print(subjects.count("Math"))
# print(subjects.count("Algebra"))


#__________________________________________________________________________________________________________________
# Loop

# for subject in subjects: # 'subject' in this loop is only a variable to reference in the loop
#     print(subject)


# for math in range(len(subjects)):
#     print(subjects[math])


chosen = 0

# while chosen < len(subjects):
#     print(subjects[chosen])
#     chosen += 1


#__________________________________________________________________________________________________________________
# Joining Tuples


digits = (1, 2, 3, 4)

names = ("Jake", "Tiffany", "William", "Bob")

# print (digits)

# print(names)

together = digits + names

# print(together)

digits_again = digits * 2

# print(digits_again)

