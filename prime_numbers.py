#Write your code below this line 👇
def prime_checker(number):
     count_down = number
     for _ in range(number):
         count_down -= 1
         if count_down > 0:
            result = number / count_down
            if result == 0:
              print("it's not prime")
            else:
              print("It is prime")      





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
