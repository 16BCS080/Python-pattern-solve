#Z paterrn
num = int( input("Enter input") )
for i in range(0, num) :
	if ( i == 0 or i == (num-1) ):
		print(num*'*')
	else:
		print( (num-i-1)*" " ,end="")
		print("*")
		

