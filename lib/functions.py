#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if (type(number) is not int and type(number) is not float): return None
    return number / 2

# check output
greet_programmer()
greet_with_default()
greet_with_default("Alice")
print(add(1, 2))
print(halve(52))