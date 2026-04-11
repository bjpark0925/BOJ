#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, m;
    cin >> n >> m;
    vector<int> arr(n);
    for (int i=0;i<n;i++){
        cin >> arr[i];
    }
    
    vector<long long> prefixSum(n+1, 0);
    for (int i=1;i<=n;i++){
        prefixSum[i] = (prefixSum[i-1] + arr[i-1]) % m;
    }
    //   1 2 3 1 2 (arr)
    //   1 3 6 7 9 (prefixSum)
    // 0 1 0 0 1 0 (m으로 나눈 나머지)
    // (psum[e] - psum[s-1]) % M = 0이면, psum[e] % M = psum[s-1] % M이 성립
    // 같은 나머지를 가진 쌍을 고르면 됨 => 0이 4개니까 4C2, 1이 2개니까 2C2
    
    vector<long long> remainder(m, 0); // remainder[0]: prefixSum에서 0의 개수 = 4, remainder[1] = 2
    for (int i=0;i<=n;i++){
        remainder[prefixSum[i]]++;
    }
    
    long long answer = 0;
    for (int i=0;i<m;i++){
        answer += remainder[i] * (remainder[i]-1) / 2; // rC2
    }
    
    cout << answer;
    
    return 0;
}