def solution(N):
    if N < 1 or N > 200000:
        raise ValueError("N is out of range")

    result = []

    # Initialize a list of lowercase letters ('a' to 'z')
    letters = list("abcdefghijklmnopqrstuvwxyz")

    # Determine the maximum number of letters you can use
    max_letters = min(N, 26)

    while N > 0:
        # Calculate the number of repetitions for each letter
        repetitions = N // max_letters

        if repetitions == 0:
            repetitions = 1  # Ensure at least one repetition

        for i in range(max_letters):
            result.append(letters[i] * repetitions)
            N -= repetitions

    return ''.join(result)

# Example usage:
N = 27
print(solution(N))
