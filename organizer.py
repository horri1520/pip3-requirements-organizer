o = open("./requirements.txt", "r")

data = o.readlines()

for i in data:
	i = i.split("=")
	print(i[0])
