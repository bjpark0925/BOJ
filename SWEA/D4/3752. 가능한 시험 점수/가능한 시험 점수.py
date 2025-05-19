T = int(input())
for t in range(T):
    N = int(input())
    score_list = list(map(int, input().split()))
    result_set = set()
    result_set.add(0)

    def calculate(temp_set, score):
        for total in temp_set:
            result_set.add(total + score)

    for score in score_list:
        calculate(result_set.copy(), score)

    #print(result_set)
    print("#{} {}".format(t+1, len(result_set)))
