#Write a FizzBuzz program counting from from 0 to 50. For multiples of 3 print "Fizz" instead of the number, and for multiples of 5 print "Buzz". 
#For numbers which are multiples of both 3 and 5 print "FizzBuzz".
#Print out each number from 1 to 50
#Print the number digits, not the text representation
#Print each number on a separate new line

for n in range(0,50):

    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)