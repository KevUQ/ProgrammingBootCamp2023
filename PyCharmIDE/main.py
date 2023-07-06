

from random import *


def maths_quiz():
    # Generate some random number
    n = randint(1, 10)

    # calculate the sum of the first n numbers
    correct_ans = 0
    for i in range(n + 1):
        correct_ans = correct_ans + i

    print('sum of first', n, 'is', correct_ans)

    user_ans = int(input(f"what is the sum of the first {n} numbers? "))

    if user_ans == correct_ans:
        print(f"You are right! the sum of the first {n} numbers is {user_ans}")
    else:
        print(f"You are wrong! the sum of the first {n} numbers is ≠ {user_ans} it is {correct_ans}")


