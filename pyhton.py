# -*- coding: utf-8 -*-
"""

@author: adnan_ahmed
"""
#%%
import random
import time
import numpy as np

#%%

#Blueprint for the car

class Car:
    
    "Car Blueprint"
    
    def __init__(self, model, color, company, speed_limit):
        self.model=model
        self.color = color
        self.company = company
        self.speed_limit= speed_limit
        
    def start(self):
        print("started")
        
    def stop(self):
        print("stopped")
        
    def accelarate(self):
        print("accelerating 1 2 3 :")
    
    def change_gear(self):
        print("gear changed")




a = Car('ertiga' , 'red', 'maruti' , '70')

a.start()
a.accelarate()
a.change_gear()
a.stop()



#%%


class rectangle:
    
    "area of rectangle"
    
    def __init__(self, length, breadth, unit_cost = 0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost
    
    def area(self):
        return self.length * self.breadth
        
    def cost(self):
        area1 = self.area
        return area1 * self.unit_cost
        #print("the total cost of the rectange is : {0}".format(self.cost))
    

a = rectangle(32,45, 20)
a.area()
a.cost()

#%%

age = int(input("what is your age?:"))
if age>18:
    print("you are eligible to vote.!")
    left=int(65-age)
    print("you still have %d years to retire" % left)
elif age>1 :
    print("you still have %d years to retire" % left)
    
else :
    print("you cant vote")

#%%
def ifinrange():    
    number = int(input("input a number in the range of 1 to 20: "))
    
    if 1<number<20:
        print("number is in the range")
    elif number <1:
        print("too low")
    elif number >20:
        print("too high")
    
#%%%

teamA = str(input("input the name of the first football team:"))

teamB = str(input("input the name of the second football team:"))

score1 = int(input("score of the %s team :" % teamA))
score2 = int(input("score of the %s team :" % teamB))

if score1 >score2:
    print("%s gets 3 point" % teamA)
    print("%s gets 0 point" % teamB)
elif score1 < score2:
    print("%s gets 3 point" % teamB)
    print("%s gets 0 point" % teamA)
elif score1 == score2:
    print("%s1 and %s2 gets 1 point each" %('teamA' ,'teamB'))
    
     
#%%

print("You are trying to find your way through a maze to the centre where ")
print("there is a pot of gold!")
print("What you don't know is that this is a dangerous maze with traps and hazards.")
print()
print("Starting maze game ...")
print()
print("You enter the maze...")
time.sleep(2) # time.sleep is just used to build up the suspense!
print("You reach a opening in the wall and go through it...")
print()
time.sleep(2)
print("You can go left (L) or right (R)")
answer = input("Make your choice ... ")
print("You chose",answer,"... what will happen? ...")
time.sleep(2)
print("You turn the corner...")
time.sleep(2)
print("You walk forward a few steps...")
time.sleep(2)
if answer == "R":
    print("you moved into a Dark alley ")
else:
    print("You moved into space")
print()
print("You can go left (Lr) or right (R)")
answer = input("Make your choice ... ")
print(" You turn the corner...")
time.sleep(2)
print("You walk forward a few steps...")    
time.sleep(2)
print("You can go left (L) or right (R)")
answer = input("Make your choice ... ")
if answer == "R":
    random.randint(1,3)
    if 1 :
        print("moved ahead")
    elif 2:
        print("reached the pot of gold")
    else :
        print("reached the trap")
        
        
#%%
        
        
month = str(input("Enter the month:?"))

winter = ['jan','feb','march']
summer = ['april', 'may','june']
spring = ['july','aug','sep']
autumn = ['oct','nov','dec']
if month in winter:
    print("YEs it is winter")
elif month in summer:
    print("YEs it is summer")
elif month in spring:
    print("YEs it is spring")
elif month in autumn:
    print("YEs it is autumn")

#%%

switch = str(input("turn the light ON or OFF?:"))

if switch == "ON":
    print("the light is turned ON")
else:
    print("the light is turned OFF")

#%%B fOR lOOPS
    
message = str(input("type the message:"))
number = int(input("the number of times you want it to be displayed?:"))
counter = 0
for number in range(number):
    print(message)

#%%
message = int(input("Enter the total numbers you want to be averaged:"))

A = []
counter =0
for counter in range(message):
    counter+=1
    A.append(counter) 
print(A)    

total = int(np.sum(A))
length = int(np.len(A))
average = int(total/length)

print("Average: %s" % average)

#%%%

message = int(input("Enter the total numbers you want to be averaged:"))


for i in range(message):
    sum =+ i
    values = int(i)

average= int(sum/values)

print("Average: %s" % average)     

#%%
right_answer=0
print("Here is a quiz to test your knowledge of farming...")
print()
print()
print("Question 1")
print("What percentage of the land is used for farming?")
print()
print("a. 25%")
print("b. 50%")
print("c. 75%")
answer = input("Make your choice: ")
if answer == "c":
    print("Correct!")
else :
    print("Wrong answer")
    time.sleep(1)
    print("youll get another shot at this")
    time.sleep(1)
    print("What percentage of the land is used for farming?")
    print()
    print("a. 25%")
    print("b. 50%")
    print("c. 75%")
    answer = input("Make your choice: ")
    if answer == "c":
        print("Correct!")
        right_answer +=1
    else :
        print("Wrong answer, Its a Shame")
time.sleep(2)        
print("lets move on to the next question")
print("Which of these is not true? Wheat is used to make,")
print("a. plastic\
      b. bread\
      c. carpets")
answer=str(input("Your answer?"))

if answer == "c":
    print("You are FuC**N Right")
    right_answer+=1
else :
    print("AWWW:")
print("you got %s right answers" % right_answer)

#%%

number = int(input("Enter the Number:"))

A = []
for count in range(number):
    count +=1
    A.append(count)
    print("{} squared is {}".format(count,count*count))
print(A)


#%%

print("starting to Add the numbers untill infinity")

A=[]
upto = int(input("UPTO?"))
while True:
    for count in range(upto):
        print(count)
        A.append(count)
        total = np.sum(A)
        print("Total until now: %s" % total)
        time.sleep(0.5)
    
#%%


l1 = ["wheat", "rye", "maize", "linseed"]
l2 = ["wheat", "rye", "maize", "linseed"]



def mystery():
    animals =["dog","cat","fox","rabbit","deer","pig"]
    for counter in range (len(animals)):
        print("Animal {0} is {1}".format(counter,animals[counter]))

a = mystery()

#%%
def animals():
    l5=[]
    for counter in range(6):
        n1 = str(input("Input the names of ananimal:"))
        l5.append(n1)
        
    print(l5)
    
    message = int(input("do you want the list in reverse order?:"))
    
    if message == 1:
        l6 = l5.reverse()
        print(l6)
    else:
        print("order not reversed")
        
    message2= int(input("choose a number between 1 and 6 "))
    
    print("the chosen animal is {}".format(l5[message2]))    
 
#%%

def divisibleby7():
    def inputData():
        number=int(input("input number:"))
        return number
    
    def processData(number):
        if number % 7 == 0:
            return True
        else:
            return False
    
    def outputData(number, result):
        if True:
            return print(" %s divisible by 7" % number)
        elif False:
            return print("%s not divisible by 7" % number)
    def main():
        userNumber = inputData()
        result = processData(userNumber)
        outputData(userNumber,result)
        
    return main()    


#%%

text = int(input("CHOOSE THE PROGRAM THAT I HAVE WRITTEN SO FAR: \n 1.animals \n 2.divisibility \n 3. if in range "))
time.sleep(0.5)

if text == 1:
    animals()
elif text ==2 :
    divisibleby7()
elif text ==3 :
    ifinrange()
else:
    print("THIS IS NOTR A VALID CHOICE, CHOOSE AGAIN")



        
#animals()
#divisibleby7()
#ifinrange()






















