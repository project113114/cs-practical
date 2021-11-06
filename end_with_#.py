f = open("sample.txt" , "r")
text = f.read()

for i in text.split(" "):
	print(i,end="#")




f.close()