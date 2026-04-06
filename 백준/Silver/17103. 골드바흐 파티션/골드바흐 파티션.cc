#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int max_num = 1000000;
    
    vector<bool> isPrime(max_num+1, true);
    isPrime[0] = isPrime[1] = false;
    for (int i=2;i*i<=max_num;i++){
        if (isPrime[i])
            for (int j=i*i;j<=max_num;j+=i){
                isPrime[j] = false;
            }
    }
    
    int t;
    cin >> t;
    for (int i = 0; i<t;i++){
        int x;
        cin >> x;
        
        int answer = 0;
        for (int j=2;j<=x/2;j++){
            if (!isPrime[j]) continue;
            if (isPrime[x-j]) answer++;
        }
        
        cout << answer << "\n";
    }
    
    return 0;
}