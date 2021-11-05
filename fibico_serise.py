n = int(input("enter the range "))
last= 0
new =1
for i in range(1,n+1):
	sum = last + new 
	last = new
	new = sum
	print(sum)
	