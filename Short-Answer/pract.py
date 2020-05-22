def one(n):
    a = 0
    while (a < n * n * n):
        a = a + n * n
        print(a)
    
# linear - contingent on n

def two(n):
    sum = 0
    for i in range(n):
        print("I:", i)
        j = 1
        while j < n:
            j *= 2
            print("J:",j)
            sum += 1
    return "Sum:", sum

# one(5)
# print(two(3))


def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    print("v", bunnies)
    return 2 + bunnyEars(bunnies-1)

print(bunnyEars(5))