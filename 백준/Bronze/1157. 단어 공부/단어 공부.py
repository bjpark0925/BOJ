word=input()
alphabet_cnt=[0 for i in range(26)]
for i in range(len(word)):
  if (ord(word[i])>=ord('A') and ord(word[i])<=ord('Z')):
    alphabet_cnt[ord(word[i])-ord('A')]+=1
  else:
    alphabet_cnt[ord(word[i])-ord('a')]+=1

max=0
for i in range(26):
  if(max==0):
    if(alphabet_cnt[i]!=0):
      max=alphabet_cnt[i]
      alphabet=chr(ord('a')+i)
  else:
    if(alphabet_cnt[i]!=0):
      if(max<alphabet_cnt[i]):
        max=alphabet_cnt[i]
        alphabet=chr(ord('a')+i)

is_max=0
for i in range(26):
  if(alphabet_cnt[i]==max):
    is_max+=1

if(is_max>=2):
  print("?")
else:
  print(alphabet.upper())
