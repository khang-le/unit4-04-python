#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program guesses random number

import random


def main():
    # this function guesses random number

    # input
    user_input = int(input("Enter a number: "))
    print("")
    # process
    nb1 = random.randint(1, 10+1)
    for loop_counter in range(user_input + 1):
        if user_input == nb1:
            break
        else:
            print("it's wrong")
            print("")
            user_input = int(input("Enter a number one"
                                   " more time from 1 - 10: "))
    print("You are correct !")


if __name__ == "__main__":
    main()
