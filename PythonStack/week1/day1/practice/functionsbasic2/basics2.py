#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

# output guess: 5



#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# output guess: error



#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# output guess: 5, 10
# outpu: 5 (once return statme is reached, the function ends and will not execute the folloing codes inside it)



#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# output guess: 5



#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# output guess: 5
# output: 5, None (5 from print(5) inside the function block. None is becuase there is no value returned in the funciton, so the value is None)



#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# output guess: 3, 5, 8
# output: 3, 5, error (TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType' // No value return in the function)



#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# output guess: 25



#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# output guss: 100, 10
# Note that return 7 will not be executed



#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# output guess: 7, 14, 21



#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# output guess: 8
# Note return 10 will not be executed.



#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

# output guess: 500, 500, 300, 500
# Note the variable in a def funciton is not related to those outside of it.



#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# output guess: 500, 500, 300, 500



#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# output guess: 500, 500, 300, 300



#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# output guess: 1, error (?)
# output: 1, 2, 3



#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# output guess: 1, 3, 5, 10