#Write your code below this line 👇
def prime_checker(number):
    primes = [2,3,5,7]
    if number in primes:
        print("It is prime")
    elif number % 2 ==0 :
        print("It is not prime ")
    elif number % 3 == 0:
        print("It is not prime ")
    elif number % 5 == 0:
        print("It is not prime ") 
    elif number % 7 == 0:
        print("It is not prime ")  
    else :
        print("It is prime")

        



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
