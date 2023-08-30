arr=[-1 for i in range(26)]
s=input()
for i in range(len(s)):
  if (arr[ord(s[i])-ord('a')]!=-1):
    continue
  arr[ord(s[i])-ord('a')]+=i+1
for i in range(len(arr)):
  print("{} ".format(arr[i]),end='')