T = 10
for tc in range(T):
    dump_cnt = int(input())
    boxes = list(map(int, input().split()))

    max_index, min_index = 0, 0
    while True:
        for i in range(len(boxes)):
            if boxes[max_index] < boxes[i]:
                max_index = i
            if boxes[min_index] > boxes[i]:
                min_index = i
        if boxes[max_index] - boxes[min_index] <= 1:
            break
        if dump_cnt <= 0:
            break
        # dump
        boxes[max_index]-=1
        boxes[min_index]+=1
        dump_cnt-=1
    print("#{} {}".format(tc+1, boxes[max_index]-boxes[min_index]))
