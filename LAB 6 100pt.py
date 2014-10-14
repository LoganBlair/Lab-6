def print_factors(x):
   """This function takes a
   number and prints the factors"""

   print("The factors of",x,"are:")
   for x in range(1, x + 1):
       if x % x == 0:
           print(x)


num = int(input("Enter a number: "))

print_factors(num)