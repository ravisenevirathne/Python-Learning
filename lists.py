# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

my_list = ["January", "February", "March", 100]
print(my_list[2])
my_list.append("April")
print(my_list[3])
print(my_list)
print(len(my_list))

for x in my_list:
    print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)