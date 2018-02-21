import sys
print ("fizzbuzzV2.py".format(sys.argv[0]))
print ("User supplied {} arguments at runtime.".format(len(sys.argv)))

if len(sys.argv) > 1: 
  for arg in sys.argv[1:]:
    topnumber = arg
    
if len(sys.argv) == 1:                    
    topnumber = input("Enter a number between, say, 14 and 10000: ")
    
try:                           
  topnumber = int(topnumber)        
except ValueError:             
  print ("No, we need a number, a positive number, made of digits.")
  topnumber = int(input("Try again.  Enter a number:   "))

print
for n in range(1, topnumber+1):
	if n % 3 == 0 and n % 5 == 0:
		print('Fizz Buzz')
	elif n % 3 == 0:
		print('Fizz')
	elif n % 5 == 0:
		print('Buzz')
	else:
		print(n)