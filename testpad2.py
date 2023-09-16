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
# A = [2, 1, 1, 2, 3, 1, 4]
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


