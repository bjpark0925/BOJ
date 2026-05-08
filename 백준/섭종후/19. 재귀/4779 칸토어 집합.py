import sys
input = sys.stdin.readline

def cantor(s, start, length):
  if length == 1:
    return
  for i in range(length//3, length//3*2):
    s[start+i] = ' '

  cantor(s, start, length//3)
  cantor(s, start+length//3*2, length//3)

while True:
  try:
    n = int(input())
  except:
    break
  
  length = 3**n
  s = ['-'] * length
  cantor(s, 0, length)
  print(''.join(s)) # print(*s, sep='')
