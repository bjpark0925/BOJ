#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(int N, int number) {
    if (N == number) return 1;
    
    // dp[i] = [{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}]
    vector<set<int>> dp(9);
    
    for (int i=1;i<=8;i++){
        // 5, 55, 555 ... 추가
        int concat = 0;
        for (int j=0;j<i;j++){
            concat = concat*10 + N;
        }
        dp[i].insert(concat);
        
        // 4번째 set에 들어갈 조합 = 1-3끼리, 2-2끼리 연산
        for (int j=1;j<i;j++){
            int k = i - j;
            for (int a : dp[j]){
                for (int b : dp[k]){
                    dp[i].insert(a+b);
                    dp[i].insert(a-b);
                    dp[i].insert(a*b);
                    if (b!=0) dp[i].insert(a/b);
                }
            }
        }
        
        if (dp[i].count(number)) return i;
    }
    
    return -1;
}