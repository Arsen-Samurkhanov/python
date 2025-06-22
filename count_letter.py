#! /bin/python3

name = input("enter your name\n")
letter = input("enter the character\n")
times = name.count(letter)
position = name.find(letter)   

print(f"the character {letter} apperes {times} times at position {position}")