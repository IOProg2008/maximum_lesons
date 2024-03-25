# def F(x):
#     if x==1:
#         return 1
#     else:
#         return 10 - F(x - 1)

# print(F(5))
import math
from random import randint
print(dir(math))
print(math.sqrt(randint(1,200)))


def f(str):
    str_fmt=str.lower()
    while 'y' in str_fmt:
        str_fmt-='y'
    else:
        return len(str)


