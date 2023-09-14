# Sets cannot access with the index, only accessible using a loop
# Not in order and NO Duplicates
my_set = {"January", "February", "March"}
for element in my_set:
    print(element)

my_set.add("April")
print(my_set)