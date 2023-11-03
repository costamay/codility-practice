# def solution(A):
#     count = 0
#     new_boxes_list = []
#     current_box = A[0]
    
#     for i in range(1, len(A)):
#         if current_box == 10:
#             return current_box
#         elif current_box < 10 and A[i] > 10:
#             remaining_bricks = 10 - current_box
#         elif current_box > 10 and A[i] > 10:
#             remaining_bricks  = current_box - 10
#             A[i] = A[i] + remaining_bricks
#         # print( A[i])
#         # if A[i] == 10:
            
#         # if A[i] < 10 and A[i + 1] >  10:
            
#     #     while A[i] < 10 and A[i + 1] >  10:
#     #         A[i + 1] -= 1
#     #         A[i] += 1
#     #         count += 1
#     # return count
#         # if A[i] < 10 and A[i + 1] >  10:
# solution([7, 15, 10, 8])

def solution(A):
    total_moves = 0
    for i in range(len(A) - 1):
        if A[i] < 10:
            moves = 10 - A[i]
            A[i + 1] -= moves
            A[i] += moves
            total_moves += moves
        if A[i] > 10:
            moves = A[i] - 10
            A[i + 1] += moves
            A[i] -= moves
            total_moves += moves
    return total_moves
solution([7, 15, 10, 8])