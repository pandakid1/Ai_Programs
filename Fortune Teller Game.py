#this program is a fortune teller
import random
print("hello! welcome to the Fortune Teller Game")
name= input("whats your name:")
randNum = random.randint(1, 6)
if randNum == 1:
    print("Your future looks bright! you will get a grate job and make millions!")
if randNum == 2:
    print("Your future looks bright! you will get a boat and travel the world!")
if randNum == 3:
    print("Your future looks bright! you will get a nice car and live in riches!")
if randNum == 4:
    print("Your future looks bad... you will get a bad job and be poor")
if randNum == 5:
    print("Your future looks bad... you will lose your job ane be poor")
if randNum == 6:
    print("Your future looks bad... you will crash your car and be poor")
