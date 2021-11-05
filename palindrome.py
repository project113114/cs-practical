x = input("enter number" )
c = 0 
l = len(x)

if l%2 !=0:
	l-= 1
l/=2
l = int(l)

for i in range(1,l+1):
	if x[i-1] == x[-i]:
		c  +=1
if c == l :
	print(x ,"is palindrome")
else:
	print(x ,"is not palindrome")
	