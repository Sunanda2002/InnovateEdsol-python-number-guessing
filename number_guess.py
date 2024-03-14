import random

lower=0
higher=0
count=0
target_num=random.randint(1,30)

print("welcome to number guessing game")
while True:
        guess=int(input("enter a number"))     
        if target_num<guess:
            print("you entered too higher number!,enter a lower number")
            higher=higher+1
        elif target_num>guess:
            print("you enterd too lower number!,enter a greater number")
            lower=lower+1
        else:
            print("congratulations!!,you won the match")
            count=count+1
            break
print("total lower number is:",lower)
print("total higher number is:",higher)
print("number of attempt is",lower+higher+count)

            

