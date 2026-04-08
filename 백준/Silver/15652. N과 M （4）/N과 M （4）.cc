#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> v;

void dfs(int start){
    if (v.size() == m){
        for (int i=0;i<m;i++){
            cout << v[i];
            if (i < m-1) cout << " ";
            else cout << "\n";
        }
        return;
    }
    
    for (int i=start;i<=n;i++){
        v.push_back(i);
        dfs(i);
        v.pop_back();
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> m;
    dfs(1);
    
    return 0;
}