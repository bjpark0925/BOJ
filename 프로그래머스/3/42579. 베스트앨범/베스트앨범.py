def solution(genres, plays):
    answer = []
    
    genre_set = set(genres)
    genre_cnt = {} # {classic:1450, pop:3100}
    genre_play = {} # {classic:[(500, 0), (600, 1), (800, 3)]}
    for genre in genre_set:
        genre_cnt[genre] = 0
        genre_play[genre] = []
    #print(genre_cnt)
    #print(genre_play)
    
    for i in range(len(genres)):
        genre_cnt[genres[i]] += plays[i]
        genre_play[genres[i]].append((plays[i], i))
    
    #print(genre_cnt)
    #print(genre_play)
    
    ranking = []
    for genre, cnt in genre_cnt.items():
        ranking.append([cnt, genre])
    ranking.sort(reverse = True)
    #print(ranking)
    
    for _, genre in ranking:
        arr = genre_play[genre]
        arr.sort(key = lambda x: (-x[0], x[1]))
        #print(arr)
        for i in range(len(arr)):
            if i >= 2:
                break
            answer.append(arr[i][1])
    
    return answer