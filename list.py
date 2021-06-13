#list,touple,dict
#list are changeble,allow duplicate,oredered

#we can append and remove by using
#list.remove()
#list.append()
"""
lis=["bannab","cherry","apple"]

lis.remove("cherry")
print(lis)
"""
# touple not call able,not change able,allow duplictae,ordered
"""
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#print(len(fruits))
"""
#dict :-unordered,changable,not allow to duplicate
#it overwriyte the preivious value

dict={
    "name":"Ravi",
    "age":29,
    "Vehicle":"Car"
}

##first are key and another is Value
print(len(dict))
print(type(dict))
"""
x= dict['age']
print(x)

y=dict.get('name')
print(y)
"""
dict['age']='26'
print(dict)

#pop method used for removing the key
dict.pop("age")

print(dict)