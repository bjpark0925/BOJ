#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    unordered_set<string> dance;
    dance.insert("ChongChong");
    for (int i=0;i<n;i++){
        string a, b;
        cin >> a >> b;
        if (dance.count(a)){
            if (!dance.count(b)){
                dance.insert(b);
            }
        }
        else{
            if (dance.count(b)){
                dance.insert(a);
            }
        }
    }
    
    cout << dance.size();
    
    return 0;
}