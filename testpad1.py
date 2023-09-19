# array_num = [10, 11, 12, 13, 14, 16, 17, 18, 19, 20]
# print("Original array:")
# print(range(10, 20))
# for i in range(1, len(array_num)):
#     for j in range(1, len(array_num)):
#         if array_num[i] == array_num[j]:
#             print(array_num[j], end=' ')
#     #print(array_num[i], end=' ')
# print("\nMissing number in the said array (10-20): ")

# rows = 10
# for i in range(1, rows+1):
#     # nested loop
#     # to iterate from 1 to 10
#     for j in range(1, i):
#         # print multiplication
#         print("*", end=' ')
#     print('')

#
# for x in range(2, 6):
#   print(x)

# first = [2, 4, 16]
# second = [5, 6, 8]
# final = []
# for i in range(len(first)):
#     final.append(first[i] + second[i])
# print(final)

# def add_lists(list1, list2):
#     result = []
#     for i in range(len(list1)):
#         result.append(list1[i] + list2[i])
#     return result
# print(add_lists([1,1], [2,2]))


# def find_missing_numbers(arr):
#     missing_numbers = []
#
#     for i, num in enumerate(arr):
#         expected_range = range(10 + i, 21)  # Define the range for each index
#         if num not in expected_range:
#             missing_numbers.append((i, list(set(expected_range) - set(arr))))
#
#     return missing_numbers


# Finding missing number in array between 10-20
input_array = [10, 12, 13, 14, 16, 17, 19, 20, 50]
print(f"Original Array : {input_array} ")
missing_array = []
expected_range = list(set(range(10, 21)))
print(f"Expected Array : {expected_range}")
for i in expected_range:
    if i not in input_array:
        missing_array.append(i)
print(f"Missing Array: {missing_array}")

for missing_nums in missing_array:
    print(f"Missing numbers : {missing_nums}")