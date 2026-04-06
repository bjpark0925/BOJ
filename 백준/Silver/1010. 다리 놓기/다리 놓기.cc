#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    
    for (int i=0;i<t;i++){
        int n, m;
        cin >> n >> m;
        long long result = 1;
        //mCn
        if (m!=n){ // 8C6 = 8C2
            if (n > m-n){
                n = m-n;
            }
            for (int j=0;j<n;j++){
                result = result * (m-j) / (1+j);
            }
        }
        cout << result << "\n";
    }
    
    return 0;
}