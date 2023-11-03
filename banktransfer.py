def solution(R, V):
    N = len(R)
    balance_A = 0
    balance_B = 0

    for i in range(N):
        recipient = R[i]
        value = V[i]

        if recipient == 'A':
            balance_A += value
        else:
            balance_B += value

        # Ensure that the account balances do not go below 0
        if balance_A < 0:
            balance_B += abs(balance_A)
            balance_A = 0
        elif balance_B < 0:
            balance_A += abs(balance_B)
            balance_B = 0

    return [balance_A, balance_B]

result1 = solution("BAABA", [2, 4, 1, 1, 2])
# result2 = solution("ABAB", [10, 5, 10, 15])
# result3 = solution("B", [100])

print(result1)


# 100%
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