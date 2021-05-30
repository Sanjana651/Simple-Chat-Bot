#!/usr/bin/env python
# coding: utf-8

# In[4]:


def greet(bot_name, birth_year):  # bot introduction
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.\n')


def remind_name():  # your intro to bot
    print('Please, remind me your name.')
    name = input("Enter your name : ")
    print('What a great name you have, ' + name + '!\n')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input("Enter remainder of dividing your age by 3 : "))
    rem5 = int(input("Enter remainder of dividing your age by 5 : "))
    rem7 = int(input("Enter remainder of dividing your age by 7 : "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + " hehe :) !\n")


def count():  
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input("Enter a number : "))
    i = 0
    while i <= num:
        print(i, '!')
        i = i + 1

        
def test():
    print("\nLet's test your programming knowledge.")
    print("Here's a question for you :P")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    while True:
        answer = int(input("Enter you answer : "))
        if answer == 2:
            break
        else:
            print("Please, try again.\n")
    print('\nCompleted, have a nice day!\n')

def end():
    print('See you, have a nice day:D')


greet('Jarvis', '2021')  # change it as you need
remind_name()
guess_age()
count()
test()
end()


# I




