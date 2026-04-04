#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
    cin >> n;
    vector<int> dp(5001, 1e9);
    dp[0] = 0; // dp[i]는 ikg을 만드는 최소 봉지 수
    
    for (int i=1; i<=n; i++){
        if (i>=3 && dp[i-3]!=1e9){
            dp[i] = min(dp[i], dp[i-3]+1);
        }
        if (i>=5 && dp[i-5]!=1e9){
            dp[i] = min(dp[i], dp[i-5]+1);
        }
    }
    
    if (dp[n] == 1e9){
        cout << -1;
    }
    else{
        cout << dp[n];
    }
    
	return 0;
}