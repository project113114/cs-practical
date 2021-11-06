def isvowel(text):
	for j in ["a","A","e","E","i","I","o","O","u","U"] :
		if text == j:
			return True
		else:
			return False
	
		
f = open("sample.txt" , "r")
text = f.read()

v =0
c = 0
u = 0 
l = 0

for k in text:
	if isvowel(k) == True:
		v+=1
	else:
		c+=1
	if k == k.isupper():
		u+=1
	else:
		l+=1
	

print("number of vowel is ",v)
print("number of consonent is ",c)
print("number of uppercase is ",u)
print("number of lowercase is ",l)		


f.close()