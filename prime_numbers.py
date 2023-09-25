#Write your code below this line 👇
def prime_checker(number):
    count_down = 9
    primes = [2,3,5,7]
    for n in primes:
     if number == primes[n-1]:
        print("It is prime")
    while count_down >0 : 
          if number % count_down == 0 or number == count_down  :
             print("It is not prime")
          else :
              print("It is prime")   
          count_down -= 1

    



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
