# def solution(A):
#     # Implement your solution here
#     smallest_positive = 0
#
#     for i in A:
#         if i > smallest_positive:
#             smallest_positive += 1
#
#     print(smallest_positive+1)
#
# A = [-1, -3, 1, -2, 2, -1]
# solution(A)


# def solution(A):
#     # Create a set to store positive integers in A
#     positive_integers = set()
#
#     # Iterate through A and add positive integers to the set
#     for num in A:
#         if num > 0:
#             positive_integers.add(num)
#
#     # Find the smallest positive integer not in the set
#     smallest_missing = 1
#     while smallest_missing in positive_integers:
#         smallest_missing += 1
#
#     return smallest_missing


# n = 2
# a_list = ['Never', 'tell', 'me', 'the', 'odds!']
#
# # Head of the list:
# sublist = a_list[:n]
# print(sublist)
#
# # Tail of the list:
# sublist = a_list[-n:]
# print(sublist)


# def solution(A):
#     # distinctvalue = set(A)
#
#     # return len(distinctvalue)
#
#     distinct_val = []
#     result = 0
#
#     for i in A:
#         if i not in distinct_val:
#             distinct_val.append(i)
#             result += 1
#     print(distinct_val)
#     return result
#
#
#
# A = [2, 1, 1, 2, 3, 1, 4, 2, 1, 1, 2, 3, 1, 4, 2, 1, 1, 5, 2, 3, 1, 4]
# print(solution(A))


#########################################################################################################
"""
def solution(N):
    factors = 0
    i = 1

    while i*i <= N:
        if N % i == 0:
            factors += 2

            if i*i == N:
                factors -= 1

        i +=1

    return factors

print(f"number of factors : {solution(24)}")
print(f"number of factors : {solution(48)}")
print(f"number of factors : {solution(64)}")

"""

#########################################################################################################

# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a, end=" ")
#         print(b, end=" ")
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#             print(c, end=" ")
#
#
# fib(5)
#

#########################################################################################################

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
#
# print(fact(10))

#########################################################################################################


# def solution(D, X):
#     #print(D, X)
#     days = 1
#     difficulty = D[0]
#     print(len(D))
#     for i in range(1, len(D)):
#         print(i)
#         difficulty = max (difficulty, D[i-1])
#         #print(difficulty)
#         if ((D[i+1]-D[i]) <= 3):
#             days = days
#         else:
#             days += 1
#     print(days)
#
#
#
#
#
# print(solution([5,8,2,7], 3))
# #print("Hello")


def solution(S):
    cameras_count = 0
    passing_count = 0
    total_count = 0

    char_arr = []
    for ch in S:
        char_arr.append(ch)
    # print (char_arr)

    for char in range(1, len(char_arr)):
        #print(char)

        if char_arr[char] == '.':
            cameras_count += 1
        elif char == '>':
            passing_count += 1
        elif char == '<':
            passing_count += 1

        # # print(S)
        # # print(passing_count)
        # if char_arr[0] == '.':
        #     cameras_count = cameras_count
        #     print(char_arr[0])
        #     break
        # if char == '.':
        #     cameras_count = cameras_count + 1
        #
        # elif char == '>':
        #     passing_count += 1
        # elif char == '<':
        #     passing_count += 1
        # # print(passing_count)
        # # print(cameras_count)
        # total_count = passing_count + cameras_count

    return cameras_count

print(solution(".>..."))
print(solution(".>.<.>"))
print(solution(">>>.<<<"))