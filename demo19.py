fobj = open('C:\\users\\karth\\emp.csv','r')
s = fobj.read()
fobj.close()

print(type(s),len(s))
print("") # empty line
print("Display file content")
print(s)