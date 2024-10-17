# def sum_of_all(*args):
#     # print(args)
#     return sum(args)


# print(sum_of_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))






# def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} = {value}")


# print_kwargs(name="ritesh", address="kalaiya", age=23)
#*******************************************************************
# Decorater example
#*******************************************************************
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result =func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)

#*******************************************************************