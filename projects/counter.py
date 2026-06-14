def counter_factory():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter


c = counter_factory()
print(c())
print(c())
print(c())