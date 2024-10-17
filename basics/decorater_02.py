import time
def cache(func):
    cached={}
    print(cached)
    def wrapper(*args, **kwargs):
        if args in cached:
            return cached[args]
        result =func(*args, **kwargs)
        cached[args]=result
        return result
    return wrapper


@cache
def sum(a,b):
    time.sleep(4)
    return a+b

print(sum(2,3))
print(sum(2,4)) 