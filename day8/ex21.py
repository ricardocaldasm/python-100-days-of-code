# Write your code below this line 👇
def prime_checker(number):    
  den = number
  count = 0
  for _ in range(number):
    rest = number % den
    den -= 1
    if rest == 0:
      count += 1

  if count == 2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
      
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)