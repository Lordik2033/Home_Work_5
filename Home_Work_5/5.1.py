def find_prime():
    num = 1
    n = 69
    while num <= n:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num
        num += 1

def find_odd_prime(seq):
    for num in seq:
        if (num % 2) != 0:
            yield num

x = find_odd_prime(find_prime())

for i in x:
    print(i)
