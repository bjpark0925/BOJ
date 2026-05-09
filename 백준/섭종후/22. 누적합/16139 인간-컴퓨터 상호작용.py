import sys
input = sys.stdin.readline

s = input().strip()
prefixSum = [[0] * 26 for _ in range(len(s))]
'''
  a b c d e
0
1
2
3
'''
for i in range(len(s)):
  for j in range(26):
    if i == 0: break
    prefixSum[i][j] = prefixSum[i-1][j]
  prefixSum[i][ord(s[i]) - ord('a')] += 1
#print(prefixSum)

q = int(input())
for _ in range(q):
  alphabet, l, r = input().split()
  l = int(l)
  r = int(r)
  if l > 0:
    print(prefixSum[r][ord(alphabet) - ord('a')] - prefixSum[l-1][ord(alphabet) - ord('a')])
  else:
    print(prefixSum[r][ord(alphabet) - ord('a')])
