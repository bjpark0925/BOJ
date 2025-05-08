import sys
input = sys.stdin.readline

n, m = map(int, input().split())
word_dict = dict() # 단어: [개수, 길이]
for _ in range(n):
    string = input().strip()
    if len(string) < m:
        continue
    if string in word_dict:
        word_dict[string][0]+=1
    else:
        word_dict[string] = [1, len(string)]
#print(word_dict)
word_list = [[word_dict[x][0], word_dict[x][1], x] for x in word_dict] # [개수, 길이, 단어]
#print(word_list)
word_list.sort(key=lambda x: (-x[0],-x[1],x[2]))
#print(word_list)
for word in word_list:
    print(word[2])