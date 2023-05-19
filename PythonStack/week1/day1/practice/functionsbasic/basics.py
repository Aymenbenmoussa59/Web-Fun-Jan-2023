def countdown(num):
    ls = []
    while num >=0:
        ls.append(num)
        num -= 1
    return ls

print(countdown(10))


#///////////////


def print_and_return(ls):
    print(ls[0])
    return ls[1]

print(print_and_return([10,8]))



def first_plus_length(ls):
    sum = ls[0] +len(ls)
    return sum

print(first_plus_length([8,2,3,4,5, 10]))





def values_greater_than_second(ls):
    new_ls = []

    if len(ls) < 2:
        return False
    else:
        for i in range(len(ls)):
            if ls[i] > ls[1]:
                new_ls.append(ls[i])
        return new_ls, len(new_ls)

print(values_greater_than_second([5,2,3,2,1,4, 6]))
print(values_greater_than_second([10]))





def size_value(size, value):
    ls = []
    while size > 0:
        ls.append(value)
        size-=1
    return ls

print(size_value(4, 7))
print(size_value(6, 2))