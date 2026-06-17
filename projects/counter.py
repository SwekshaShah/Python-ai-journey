def counter_factory():
    count = 0
    def counter():
        while True:
            nonlocal count
            count += 1
            print(count)
        return count
    return counter


c = counter_factory()
print(c())
print(c())
print(c())