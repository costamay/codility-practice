
# 100%
def solution(A):
    # Implement your solution here
    A.sort()
    rooms = 1
    room_capacity = A[0]

    guest_in_room = 1

    for i in range(1 , len(A)):
        if guest_in_room < room_capacity:
            guest_in_room += 1

        else:
            rooms += 1
            room_capacity = A[i]
            guest_in_room = 1

    return rooms

# 72%
def solution(R, V):
    
  min_A = 0
  min_B = 0
 
  balance_A = 0
  balance_B = 0
  
  for i in range(len(R)):
    
    recipient = R[i]
    value = V[i]
    
    if recipient == "B":
      
      balance_A -= value
      balance_B += value
     
      if balance_A < min_A:
       
        min_A = balance_A
   
    else:
      
      balance_B -= value
      balance_A += value
     
      if balance_B < min_B:
       
        min_B = balance_B
  
  return [abs(min_A), abs(min_B)]

# 100%
def solution(A):
    
    # Implement your solution here
    A.sort(reverse=False)
    Numofrooms = 1
    room_cap = A[0]
    guest_in = 1
    for i in range(1,len(A)):
        if guest_in < room_cap:
            guest_in+=1
        else:
            Numofrooms +=1
            room_cap = A[i] 
            guest_in = 1
    return Numofrooms