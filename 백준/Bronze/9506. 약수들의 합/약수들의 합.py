while True:
    n = int(input())
    if (n == -1):
        break
    total = 0
    yaksu = []
    for i in range(1, n):
        if (n%i == 0):
            total += i
            yaksu.append(i)
            if (total > n):
                break;
    
    if (total == n):
        print(n, "= ", end='')
        for i in range(len(yaksu)):
            if (i == len(yaksu)-1):
                print(yaksu[i])
            else:
                print(yaksu[i], "+ ", end='')
    else:
        print(n, "is NOT perfect.")
        
                