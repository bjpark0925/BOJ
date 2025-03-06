alpha = input()
answer = 0

for i in range(len(alpha)):
    diff = ord(alpha[i])-ord('A')
    if (alpha[i]>='S'):
      diff-=1
    if (alpha[i]>='Z'):
      diff-=1
        
    answer += (diff)//3 + 3
    
print(answer)