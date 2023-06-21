my_list = []
listi = [23,12,34,21,34,21,44,45,25]
gameorebebi_listi = [22,22,33,44,44,5,6,6]
listi2 = [45,50,55,60,65,70,75]
listi3 = [1,2,[3,4],5,6,[7,8,9],10]
def max_value(some_list):
    return max(some_list)


def min_value(some_list):
    return min(some_list)

my_list2 = []
def unique(some_list):
    for i in some_list:
        if not i in my_list2:
            my_list2.append(i)



def extract(some_list):
    for i in some_list:
        if type(i) == list:
            for e in i:
                my_list.append(e)
        else:
            my_list.append(i)


def usj(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def usj_from_list(some_list):
    a = max_value(some_list)
    b = min_value(some_list)
    return usj(a, b)

print(max_value(listi))
print(min_value(listi))
unique(gameorebebi_listi)
print(my_list2)
extract(listi3)
print(my_list)
print(usj(45,75))
print(usj_from_list(listi2))



