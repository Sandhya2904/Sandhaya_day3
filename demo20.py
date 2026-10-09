fobj = open('C:\\users\\karth\\emp.csv','r')
L = fobj.readlines()
fobj.close()

print(type(L),len(L))
print("") # empty line
print("Display file content")
print(L)