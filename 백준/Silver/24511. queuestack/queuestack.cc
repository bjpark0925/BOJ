#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    vector<int> data_st(n);
    for (int i=0;i<n;i++){
        cin >> data_st[i];
    }
    
    deque<int> elem;
    for (int i=0;i<n;i++){
        int x;
        cin >> x;
        if (data_st[i] == 0){
            elem.push_back(x);
        }
    }
    
    int m;
    cin >> m;
    for (int i=0;i<m;i++){
        int c;
        cin >> c;
        
        elem.push_front(c);
        cout << elem.back();
        if (i<m-1) cout << " ";
        elem.pop_back();
    }    
    
    return 0;
}