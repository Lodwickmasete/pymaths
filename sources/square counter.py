def qrange(n):
    for i in range(1, n):
        yield i * i


n = 10
print('Squares of numbers from 1 to %d are:' % (n - 1))
for i in qrange(n):
    print(i)
