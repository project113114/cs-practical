n = int(input("enter the number of exponent "))
x = int(input("enter the base here "))
sum = 1+x
for i in range(2,n+1):
	sum += x**i
	
print("the computed result is ", sum )