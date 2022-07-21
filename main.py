print('__________________')
print('List') 
print('------------------\n')

list = [1, 2, 'hey', True, 9, 'no']

print (list[0])
print (list[1])
print (list[2])
print (list[3])

print('__________________')
print('List slising') 
print('------------------\n')

print (list)

#lists are mutable

list[1] = "new"
print (list)

print('__________________')
print('List Methods') 
print('------------------\n')

print (' \n* Adding\n ')
print(len(list))
print(list.append(100))# this does't give value because it's not creat new value just change the list
print(list)
print(list.insert(4,99))# this does't give value because it's not creat new value just change the list
print(list)
print(list.extend([223,778]))# this does't give value because it's not creat new value just change the list
print(list)

print (' \n* Removing\n ')

print(list.pop())# this pops off waht ever at the end of the list  and return the poped value
print(list)

print(list.pop(0))# this pops off the object respect to the index and return the poped value
print(list)

print(list.remove(9))# this remove given value
print(list)

print(list.clear())# this clear every thing. this does not return any value
print(list)

print('\n* Index \n')

list2 = (99, 'k', 12)

print(list2.index(99))#this finds the index respect to the value
 
print('\n* In \n') 
print(100 in list2)#check for the given value
print("i" in 'i am gihan')

print('\n* sort \n')
list3=[1,3,5,7,5,3,7,8,2]
print(list3.sort())# this modify the list. this does not return any value
print(list3)
print(sorted(list3)) #since this is a fuction it have a output

print('\n* reverse \n')
print(list3.reverse())# this modify the list. this does not return any value
print(list3)

print('__________________')
print('Matrix') 
print('------------------\n')

matrix =[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
#matrix is a multy diementional list

print(matrix[0][2])

print('__________________')
print('Dictionary') 
print('------------------\n')

dict = {
  'a' : 1,
  'b' : 2
}

print(dict['a'])
print (dict.get ('c'))# eventhough 'c' doesn't excist it dosent give an error it's good for the program
print (dict.get ('c',00))# we can give a default value 

print ('a'in dict)
print ('a' in dict.keys())
print (2 in dict.values())
print (dict.items())


print('______')
print('Tuple') 
print('------\n')

tuple = (1,2,4,6,5,4,3) # braket indidate a tuple. it is immutable.other than that it's similar to list


print('______')
print('Set') 
print('------\n')

my_set = {1,2,4,5,6,5,6}# unorded unique data set
my_set2 = {5,6,7,8,9}
my_set.add(100)
my_set.add(2)
print(my_set)
#can't call by index in a set we have find the value in the set
print(2 in my_set)
print(my_set.difference(my_set2))
my_set.discard(5)
print(my_set)
print(my_set.difference_update(my_set2))
print(my_set)
print(my_set.isdisjoint(my_set2))
print(my_set.union(my_set2))
print(my_set.issubset(my_set2))
print(my_set.issuperset(my_set2))

