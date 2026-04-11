#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    vector<int> stair(n);
    for (int i=0;i<n;i++){
        cin >> stair[i];
    }
    
    vector<int> dp(n, 0); // dp[i] = i번째 계단까지의 점수 최댓값
    dp[0] = stair[0];
    if (n>=1) dp[1] = dp[0] + stair[1];
    if (n>=2) dp[2] = max(dp[0], stair[1]) + stair[2];
    for (int i=3;i<n;i++){
        dp[i] = max(dp[i-2], dp[i-3]+stair[i-1]) + stair[i];
    }
    cout << dp[n-1];
    
    return 0;
}