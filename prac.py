import math
import random

print("0. Enter the student number:")
studentNumber = (input()) 
studentNumberList =[]
studentNumberList = list(studentNumber)

def countPrime(num):
    n =[]
    for i in num:
      if(int(i) >1):
        is_prime=True
        for j in range(2,(int(i))):
            if(int(i)%j == 0):
                is_prime=False
                break
        if(is_prime):
            n.append(i)
    return len(n)
      
def randomgen():
    return random.randint(25,51)

def generateRandom(dividedNumber):
    alpha =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    itemsToReturn = []
    for x in range(dividedNumber):
        items =[]   
        num = 6 - (-1)**x
        items = random.sample(alpha,num )
        s = "".join(items)
        print(s)
        itemsToReturn.append(s)

    return itemsToReturn

def sortList(sList):
    slist =  sorted(sList,key=lambda word: sum(vowels in 'aeiou' for vowels in word), reverse=True)
    for x in slist:
        print(x)
    return 0

numPrimeNumbers = countPrime(studentNumberList)
randomNum = randomgen()
dividedNumber = randomNum // numPrimeNumbers

stringList= []


print("The number of prime numbers is:" + str(numPrimeNumbers))
print("The random number is:"+ str(randomNum))
print("Number of string to be generated is:"+str(dividedNumber))
print("List of strings:\n*************************")
stringList = generateRandom(dividedNumber)
print("*************************")
print("Sorted list:\n*************************")
sortList(stringList)
print("*************************")