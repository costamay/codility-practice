def solution(N):
    if N <= 0:
        return ""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num_letters = min(N, 26)
    print(num_letters)
    equal_occurrences = N // num_letters
    print("equal_occurrences")
    print(equal_occurrences)
    remaining_chars = N % num_letters

    result = []

    for i in range(num_letters):
        letter = alphabet[i]
        occurrences = equal_occurrences
        if i < remaining_chars:
            occurrences += 1

        result.append(letter * occurrences)

    return ''.join(result)
print(solution(5))
print(solution(3))
print(solution(30))

