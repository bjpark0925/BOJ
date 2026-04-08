#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> v;
bool visited[9];

void dfs(){
    if (v.size() == m){
        for (int i=0;i<m;i++){
            cout << v[i];
            if (i < m-1) cout << " ";
            else cout << "\n";
        }
        return;
    }
    
    for (int i=1;i<=n;i++){
        if (visited[i]) continue;
        visited[i] = true;
        v.push_back(i);
        dfs();
        v.pop_back();
        visited[i] = false;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> m;
    dfs();
    
    return 0;
}