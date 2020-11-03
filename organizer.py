PYTHON_VERSION = '3.7.9'
OS = 'ubuntu'
o = open("./{}_{}.txt".format(PYTHON_VERSION, OS), "r")

data = o.readlines()

for i in data:
    i = i.split("=")
    print(i[0])
