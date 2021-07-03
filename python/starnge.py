def extendList(val, list1=[]):
        list1.append(val)
        return  list1
list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')
print(list1,list2,list3)

"""
([10, ‘a’], [123], [10, ‘a’])

You’d expect the output to be something like this:

([10],[123],[‘a’])

Well, this is because the list argument does not initialize to its default value ([]) every time we make a call to the function.
Once we define the function, it creates a new list. Then, whenever we call it again without a list argument, it uses the same list.
This is because it calculates the expressions in the default arguments when we define the function, not when we call it.

"""