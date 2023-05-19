# 1 print "Hello World"
print("Hello World")


# 2 print "Hello Noelle!" with the name in a variable
name = "Aymen"
print("Hello", name, "!")
print("Hello " + name + "!")


# 3 print "Hello 42!" with the number in a variable
number = 42
print("Hello", 42, "!")
print("Hello " + str(number) + "!")


# 4 print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"

print("I love eat {} and {}.".format(fave_food1,fave_food2))
print(f"I love eat {fave_food1} and {fave_food2}.")
# bonus ninja
print("Hello", str(number) + "!")
text = "Hello World"
print(text.upper())  # Output: HELLO WORLD
print(text.lower())  # Output: hello world
print(text.replace("Hello", "Goodbye"))  # Output: Goodbye World
