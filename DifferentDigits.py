def solution(A):
    # Create a list of sets to store the unique digits of each number
    digit_sets = [set(str(num)) for num in A]
    
    max_sum = -1

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            # Check if the sets of digits have no common elements
            print(digit_sets[i], digit_sets[j])
            if not digit_sets[i].intersection(digit_sets[j]):
                max_sum = max(max_sum, A[i] + A[j])

    return max_sum

# Test cases
A1 = [53, 1, 36, 103, 53, 5]
print(solution(A1))

# def have_common_digits(num1, num2):
#     digits1 = set(str(num1))
#     digits2 = set(str(num2))
    
#     return bool(digits1 & digits2)

# def solution(A):
#     max_sum = -1

#     for i in range(len(A)):
#         for j in range(i + 1, len(A)):
#             if not have_common_digits(A[i], A[j]):
#                 max_sum = max(max_sum, A[i] + A[j])

#     return max_sum