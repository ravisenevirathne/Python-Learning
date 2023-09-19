#########################################################################################################
# linear search
"""
pos = -1

def search(list, n):
    i = 0

    # while i < len(list):
    #     if list[i] == n:
    #         globals()['pos'] = i
    #         return True
    #     i += 1
    # return False

    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True


list = [2, 3, 4, 5, 6, 7, 8]
n = 8

if search(list, n):
    print(f"Found at index : {pos}")
else:
    print("Not found in list")

"""
#########################################################################################################
#Bnary Search



#########################################################################################################
#Bubble sort
# def sort_algo(nums):
#     for i in range(len(nums)-1, 0, -1):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
#
#
# nums = [5, 4, 3, 8, 4, 7, 1, 0]
# sort_algo(nums)
# print(nums)

#########################################################################################################
#Selection sort

# def sort_algo(nums):
#     for i in range(len(nums)):
#         minpos = i
#         for j in range(i+1, len(nums)):
#             if nums[j] < nums[minpos]:
#                 minpos = j
#
#         temp = nums[i]
#         nums[i] = nums[minpos]
#         nums[minpos] = temp
#
# nums = [2, 5, 4, 3, 8, 4, 7, 1, 0]
# sort_algo(nums)
# print(nums)

#########################################################################################################

