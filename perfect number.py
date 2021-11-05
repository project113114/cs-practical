n  = int(input("enter the number to cheack "))
sum = 0
for i  in range(1,n):
	if n%i == 0:
		sum += i 
if sum == n:
	print(n, " is perfect number")
else:
	print(n , " is not perfecr number")