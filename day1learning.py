"""
today I learnt about lists [], sets {} and sets.
lists are immutable.
"""
x=[1,2,3,4,5]
print(x)
print(type(x))
x[3]=20
print(x)
'''
to print a certain number or value we use n-1
i.e we start counting from zero .
lists can also include strings. or you can mix both strings and integers on the same list.
list can contain more than one list i.e
'''
mix=[["jhn","amos","peter"],["today",1,2,3,4]]
print(type(mix))
print(mix)
num=["clinton","Nyamare" ,"orenge", "faith", "bosibori"]
print(type(num))
#to access the elements in a list using indexing a range of elements.
print(num[0:3])
''''
you can change the value of a list by;
to replace "orenge" with "MOM"
'''
num[2]="MOM"
print(num)
'''
when accessing the elements in a list when we start from the front we start from zero,
 while when we start from the end we start from -1, example.
'''
print(num[-1])
#it returns bosibori.
''''
to get a value at a certain interval, lets say at an interval of 2 we use[::x]
x is the interval value example;
'''
inter=[1,2,3,4,10,5,6,7,8,8,9,6,4,5,7,"maths","english","biology"]
print(inter[0::2])
#this line means print from the start of the list(you can neglect the 0) to the last value of the list
#at an interval of 2.
'''
you can use the -1 to print the list in a revers order.
the [::x] i this case is used to reorder from the last to the start.
'''
print(inter[::-1])

'''
lists also help save time lest say you what to print a certain string or a number n times
you can do this;
'''
Z=["CLINTON"]*10
print(Z)

#to add/concatenate a list you just use a '+'
conc=Z + inter
print(conc)
# to add a value to your list you use .append, on typing the var and adding . a dropdown list is available
# to choose from
# example
#to add a list to a list use the .extend() followed by the list name you want to add.
Z.append("kemoda")
print(Z)
#to add a value at a certain level use the .insert
Z.insert(4,"MAGUTE")
print(Z)

'''
               TUBULES
they are immutable- they cannot be changed
we use ()
most of the commands that work with lists work in tubules. Play around with it.
'''
