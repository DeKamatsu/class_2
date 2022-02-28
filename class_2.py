# 2-nd lesson. Variables. I/O

#print (round(1.1245, 4))
#name = 'fdgh\n'
#print(name * 5)
#print (name[-2])
#print (name[2:])
#print (name[:2])

#print(len(name))

#print(format("String is %name"))
#print(f"String is {name}")
""""
if not(1 != 1):
    print(1)
else:
    print(2)

d = ['a', 'b', 'c']
print(d)

name = "Denis"
print(list(name)[:2])
print(list(name)[2:])
print(list(name)[::2])

del name[3]
print(name)
"""
list_1 = [1 , 2, "asf", "sd", False, True, 2, 2]
i = list_1.index(2)+1
print(list_1[
            list_1.index(2)+1:]
            .index(2))