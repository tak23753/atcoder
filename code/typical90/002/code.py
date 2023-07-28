
from itertools import product

def check(str):
    score = 0

    for char in str:
        if char == '(':
            score += 1
        elif char == ')':
            score -= 1

        if score < 0:
            return False

    return (score == 0)

N = int(input())
for pro in product(('(', ')'), repeat=N):
        if (check(pro)):
            print(*pro, sep='')
