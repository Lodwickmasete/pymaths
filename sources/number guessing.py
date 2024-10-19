import random

maxn = 10
n = random.randint(1, maxn)
print('Welcome to guess the number game!')
print('Guess the number from 1 to %d' % maxn)
guess = None
while guess != n:
    guess = int(input('Your try: '))
    if guess > n:
        print('Too high')
    if guess < n:
        print('Too low')

print('Congratulations, you won!')
