def solution(s):
    related_letters = {   
    }
    
    unique_chars = set()
    
    for char in s:
        if char.lower() in related_letters:
            related_letters[char.lower()] += char 
        else:
            related_letters[char.lower()] = char
            
    
    for i in related_letters:
        if related_letters[i][0].islower():
            for j in related_letters[i][1:]:
                # print(related_letters[i][-1])
                if j.isupper() and related_letters[i][-1] != related_letters[i][0]:
                    unique_chars.add(j)
                    
    
    return len(unique_chars)
    
chars = solution('aaAbcCABBc')
print(chars)