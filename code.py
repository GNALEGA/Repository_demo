def exercice1():
	"""############################ Exercice 1 ############################################
	#program which concatenates 2 strings and prints the resulting unified string with
	#the EOF character at the end of it. The 2 inputstrings are asked by the program"""

    

	str1=input('Please enter the first string value:')
	str2=input('Please enter the second string value:')
  print("{first}{second}".format(first=str1,second=str2)).*

def exercice2():
	"""############################ Exercice 2 ############################################
	#  asks for a number to the user"""

	print("[Exercice 2]")

	value=int(input('Please enter a number:'))

	# output wether X is odd or even
	if value%2 == 0:
	    print( 'Even number')
	else:
	    print( 'Odd number' )
