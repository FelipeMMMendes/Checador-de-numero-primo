#Write your code below this line 👇
def prime_checker(number):
    Isprime = 1
    for n in range(2,number):
        if number%n==0:
            Isprime = 0
            
    if Isprime == 1:
        print("It's a prime number") 
    else:
        print("It's not a prime number")               

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
