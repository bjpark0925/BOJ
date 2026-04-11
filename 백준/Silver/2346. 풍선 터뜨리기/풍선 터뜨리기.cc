#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    deque<pair<int, int>> dq; // {인덱스, 값}
    for (int i=1;i<=n;i++){
        int val;
        cin >> val;
        dq.push_back({i, val});
    }
    
    while (!dq.empty()){
        auto [idx, val] = dq.front();
        dq.pop_front();
        cout << idx << " ";
        
        if (dq.empty()) break;
        
        if (val > 0){
            rotate(dq.begin(), dq.begin()+(val-1)%dq.size(), dq.end());
        }
        else{
            rotate(dq.begin(), dq.end()-(-val)%dq.size(), dq.end());
        }
    }
    
    return 0;
}