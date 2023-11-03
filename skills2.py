# def solution(A):
#     freqSkills = {}
#     templist = []
#     a, b = 0, 0
#     for i, v in enumerate(A):
#         if v not in freqSkills:  # initial Round (1)
#             freqSkills[v] = 1
            
#         else:
#             freqSkills[v] += 1
            
#                 a = A[i]
#                 b = A[i + 1]
#                 templist.append(max(a, b))
#         # a, b = v, A[i+1]
#         # max_v = max(a, b)
#         # templist.append(max_v)
#     print(freqSkills, 'freqSkills')
#     print(templist, 'templist')

def solution(skills):
   ar = list(skills)
   t = {}
   r = 1
   while True:
       if len(ar) == 0 or len(ar) == 1:
           sol_ar = []
           for s in skills:
               sol_ar.append(t.get(s, r - 1))
           return sol_ar
       s = complete_round(ar, r, t)
       ar = s['a']
       r += 1

def complete_round(skills, round=1, t={}):
   new_arr = []
   for i in range(1, len(skills), 2):
       player1 = skills[i - 1]
       player2 = skills[i]
       if player1 is None or player2 is None:
           new_arr.append(player1 if player1 else player2)
           t[player1 if player1 else player2] = round
           continue
       if player1 > player2:
           new_arr.append(player1)
           t[player2] = round
           continue
       t[player1] = round
       new_arr.append(player2)
   return {'a': new_arr, 't': t}
print(solution([4,2,7,3,1,8,6,5]))
print(solution([4,2,1,3]))